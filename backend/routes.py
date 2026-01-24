from flask import Blueprint, jsonify, request ,  render_template
from llm_router import llm_pick_best_query
from db import fetch_all, fetch_one
from queries import (
    GET_STORE_BY_ID,
    SEARCH_PRODUCTS,
    GET_COUPON_BY_STORE,
    GET_BEST_AD_BY_STORE,
    GET_ROUTE_BY_STORE,
    GET_SUGGESTIONS,
)

_SESSIONS = {}

api_bp = Blueprint("api", __name__)

def _get_session(session_id: str):
    if session_id not in _SESSIONS:
        _SESSIONS[session_id] = {
            "stage": "searching",
            "selected_store_id": None,
            "last_text": None,
        }
    return _SESSIONS[session_id]

def _response(session_id: str, messages=None, store_buttons=None, coupon_buttons=None, coupon_code=None, ad=None):
    return {
        "session_id": session_id,
        "messages": messages or [],
        "ui": {
            "store_buttons": store_buttons or [],
            "coupon_buttons": coupon_buttons or [],
        },
        "data": {
            "coupon_code": coupon_code,
            "ad": ad,
        },
    }

@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@api_bp.route("/stores", methods=["GET"])
def get_stores():
    return jsonify({"status": "ok"})


@api_bp.route("/", methods=["GET"])
def home():
    return render_template("chat.html")


@api_bp.route("/coupon", methods=["GET"])
def coupon_page():
    return render_template("coupon.html")


@api_bp.route("/navigate", methods=["GET"])
def navigate_page():
    return render_template("navigate.html")

@api_bp.route("/chat/message", methods=["POST"])
def chat_message():
    payload = request.get_json(force=True)
    session_id = payload.get("session_id", "default")
    text = (payload.get("text") or "").strip()
    limit = int(payload.get("limit", 10))

    sess = _get_session(session_id)
    sess["stage"] = "searching"
    sess["last_text"] = text

    if not text:
        messages = [{
            "role": "assistant",
            "text": "מה מחפשים? כתוב מוצר או קטגוריה (למשל: משקפי שמש, קפה, נעליים)."
        }]
        return jsonify(_response(session_id, messages=messages))

    rewritten = llm_pick_best_query(text, [])
    queries = rewritten.get("queries") or [text]

    print("LLM queries:", queries)

    rows = []
    for q in queries:
        p = f"%{q}%"
        rows = fetch_all(SEARCH_PRODUCTS, (p, p, p, limit))
        if rows:
            break

    if not rows:
        pattern = f"%{text}%"
        candidates = fetch_all(GET_SUGGESTIONS, (pattern, 20))
        terms = [r["term"] for r in candidates]

        if terms:
            rewritten2 = llm_pick_best_query(text, terms)
            queries2 = rewritten2.get("queries") or []
            for q in queries2:
                p = f"%{q}%"
                rows = fetch_all(SEARCH_PRODUCTS, (p, p, p, limit))
                if rows:
                    break

    queries = rewritten.get("queries") or [text]

    rows = []
    used_query = text 
    for q in queries:
        if not isinstance(q, str):
            continue
        q = q.strip()
        if not q:
            continue

        used_query = q
        p = f"%{q}%"
        rows = fetch_all(SEARCH_PRODUCTS, (p, p, p, limit))
        if rows:
            break

    if not rows:
        messages = [{
            "role": "assistant",
            "text": f"לא מצאתי תוצאות עבור: {text}. נסה ניסוח אחר או שם קטגוריה."
        }]
        return jsonify(_response(session_id, messages=messages, store_buttons=[]))

    seen = set()
    store_buttons = []
    for r in rows:
        sid = r["store_id"]
        if sid not in seen:
            seen.add(sid)
            store_buttons.append({"store_id": sid, "store_name": r["store_name"]})

   
    return jsonify(_response(session_id, store_buttons=store_buttons))


@api_bp.route("/chat/store-click", methods=["POST"])
def chat_store_click():
    payload = request.get_json(force=True)
    session_id = payload.get("session_id", "default")
    store_id = int(payload["store_id"])

    sess = _get_session(session_id)
    sess["selected_store_id"] = store_id
    sess["stage"] = "coupon_prompt"

    store = fetch_one(GET_STORE_BY_ID, (store_id,))
    store_name = store["store_name"] if store else f"חנות #{store_id}"

    messages = [{"role": "assistant", "text": f"בחרת: {store_name}. רוצה קופון?"}]
    coupon_buttons = [
        {"answer": "yes", "label": "כן"},
        {"answer": "no", "label": "לא"},
    ]

    return jsonify(_response(session_id, messages=messages, coupon_buttons=coupon_buttons))


@api_bp.route("/chat/coupon", methods=["POST"])
def chat_coupon():
    payload = request.get_json(force=True)
    session_id = payload.get("session_id", "default")
    store_id = int(payload["store_id"])
    answer = (payload.get("answer") or "").strip().lower()

    sess = _get_session(session_id)
    sess["selected_store_id"] = store_id
    sess["stage"] = "end"

    best_ad = fetch_one(GET_BEST_AD_BY_STORE, (store_id,))
    ad_obj = None
    if best_ad:
        ad_obj = {
            "ad_id": best_ad["ad_id"],
            "ad_type": best_ad["ad_type"],
            "asset_url": best_ad["asset_url"],
            "trigger": best_ad.get("trigger"),
        }

    if answer == "yes":
        coupon = fetch_one(GET_COUPON_BY_STORE, (store_id,))
        coupon_code = coupon["coupon_code"] if coupon else None

        if coupon_code:
            messages = [{"role": "assistant", "text": f"הקופון שלך: {coupon_code}"}]
        else:
            messages = [{"role": "assistant", "text": "אין קופון זמין כרגע לחנות הזו (MVP), אבל אפשר להמשיך לנווט."}]

        return jsonify(_response(session_id, messages=messages, coupon_code=coupon_code, ad=ad_obj))

    messages = [{"role": "assistant", "text": "מנתב לניווט."}]
    return jsonify(_response(session_id, messages=messages, coupon_code=None, ad=ad_obj))


@api_bp.route("/nav/route", methods=["GET"])
def nav_route():
    store_id = request.args.get("store_id", type=int)
    if not store_id:
        return jsonify({"ok": False, "error": "missing store_id"}), 400

    row = fetch_one(GET_ROUTE_BY_STORE, (store_id,))
    if not row:
        return jsonify({"ok": False, "error": "route not found"}), 404

    return jsonify({
        "ok": True,
        "store_id": row["store_id"],
        "map_target_id": row["map_target_id"],
        "route_path_d": row["route_path_d"],
    })
