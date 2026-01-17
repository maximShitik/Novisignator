const form = document.getElementById("chatForm");
const input = document.getElementById("chatInput");
const messages = document.getElementById("messages");

const storesMessage = document.getElementById("storesMessage");
const storeChips = document.getElementById("storeChips");
const couponQuestion = document.getElementById("couponQuestion");
const statusPill = document.getElementById("statusPill");

const API_BASE = ""; // same origin (Flask serves the page)
const LS_SESSION_KEY = "sns_session_id";
const LS_SELECTED_STORE_ID = "sns_selected_store_id";
const LS_SELECTED_STORE_NAME = "sns_selected_store_name";
const LS_COUPON_CODE = "sns_coupon_code";

function getSessionId() {
  let sid = localStorage.getItem(LS_SESSION_KEY);
  if (!sid) {
    sid = "s_" + Math.random().toString(36).slice(2, 10);
    localStorage.setItem(LS_SESSION_KEY, sid);
  }
  return sid;
}

function setStatus(text) {
  if (statusPill) statusPill.textContent = text;
}

function addMessage(text, who) {
  const msg = document.createElement("div");
  msg.className = `msg ${who}`;

  const bubble = document.createElement("div");
  bubble.className = "bubble";
  bubble.textContent = text;

  const meta = document.createElement("div");
  meta.className = "meta";
  meta.textContent = who === "user" ? "אתה" : "בוט";

  msg.appendChild(bubble);
  msg.appendChild(meta);
  messages.appendChild(msg);

  messages.scrollTop = messages.scrollHeight;
}

async function postJson(path, body) {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  return await res.json();
}

function showStores(stores) {
  storeChips.innerHTML = "";

  stores.forEach((s) => {
    const btn = document.createElement("button");
    btn.className = "chip";
    btn.type = "button";
    btn.textContent = s.store_name;

    btn.addEventListener("click", async () => {
      const session_id = getSessionId();

      // save selection for other pages
      localStorage.setItem(LS_SELECTED_STORE_ID, String(s.store_id));
      localStorage.setItem(LS_SELECTED_STORE_NAME, s.store_name);

      addMessage(`בחרתי: ${s.store_name}`, "user");
      setStatus("שולח...");

      const resp = await postJson("/chat/store-click", {
        session_id,
        store_id: s.store_id,
      });

      // show bot message(s)
      (resp.messages || []).forEach((m) => addMessage(m.text, "bot"));

      // show coupon question + build buttons dynamically
      renderCouponButtons(resp);
      setStatus("מוכן");
    });

    storeChips.appendChild(btn);
  });

  // move + show stores block
  messages.appendChild(storesMessage);
  storesMessage.hidden = false;
  messages.scrollTop = messages.scrollHeight;
}

function renderCouponButtons(resp) {
  // Coupon question block contains .actions with <a> links in your HTML.
  // We'll replace them with real buttons that call the API.
  const actions = couponQuestion.querySelector(".actions");
  actions.innerHTML = "";

  const buttons = (resp.ui && resp.ui.coupon_buttons) ? resp.ui.coupon_buttons : [
    { answer: "yes", label: "כן" },
    { answer: "no", label: "לא" }
  ];

  buttons.forEach((b) => {
    const btn = document.createElement("button");
    btn.className = b.answer === "yes" ? "btn primary" : "btn secondary";
    btn.type = "button";
    btn.textContent = b.label;

    btn.addEventListener("click", async () => {
      const session_id = getSessionId();
      const store_id_str = localStorage.getItem(LS_SELECTED_STORE_ID);
      const store_id = store_id_str ? parseInt(store_id_str, 10) : null;

      if (!store_id) {
        addMessage("לא נמצאה חנות נבחרת. בחר חנות קודם.", "bot");
        return;
      }

      setStatus("שולח...");

      const resp2 = await postJson("/chat/coupon", {
        session_id,
        store_id,
        answer: b.answer,
      });

      // save coupon if exists
      if (resp2.data && resp2.data.coupon_code) {
        localStorage.setItem(LS_COUPON_CODE, resp2.data.coupon_code);
      } else {
        localStorage.removeItem(LS_COUPON_CODE);
      }

      // optional: save ad info too (for future)
      // localStorage.setItem("sns_ad", JSON.stringify(resp2.data?.ad || null));

      // decide where to go
      if (b.answer === "yes") {
        window.location.href = "coupon.html";
      } else {
        window.location.href = "navigate.html";
      }
    });

    actions.appendChild(btn);
  });

  messages.appendChild(couponQuestion);
  couponQuestion.hidden = false;
  messages.scrollTop = messages.scrollHeight;
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const text = input.value.trim();
  if (!text) return;

  // hide previous blocks
  storesMessage.hidden = true;
  couponQuestion.hidden = true;

  addMessage(text, "user");
  input.value = "";

  setStatus("מחפש...");
  addMessage("מחפש... רגע ", "bot");

  const session_id = getSessionId();

  const resp = await postJson("/chat/message", {
    session_id,
    text,
    limit: 10,
  });

  // show bot message(s)
  (resp.messages || []).forEach((m) => addMessage(m.text, "bot"));

  const stores = (resp.ui && resp.ui.store_buttons) ? resp.ui.store_buttons : [];
  if (stores.length > 0) {
    showStores(stores);
  }

  setStatus("מוכן");
});
