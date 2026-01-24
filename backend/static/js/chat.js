(() => {
  const qs = (sel, root = document) => root.querySelector(sel);

  const form = qs("#chatForm");
  const input = qs("#chatInput");
  const messages = qs("#messages");
  if (!form || !input || !messages) return;

  const storesMessage = qs("#storesMessage");
  const storeChips = qs("#storeChips");
  const couponQuestion = qs("#couponQuestion");
  const statusPill = qs("#statusPill");

  const LS = {
    SESSION: "sns_session_id",
    STORE_ID: "sns_selected_store_id",
    STORE_NAME: "sns_selected_store_name",
    COUPON_CODE: "sns_coupon_code",
  };

  if (storesMessage) storesMessage.hidden = true;
  if (couponQuestion) couponQuestion.hidden = true;

  const scrollToBottom = () => {
    messages.scrollTop = messages.scrollHeight;
  };

  const setStatus = (text) => {
    if (statusPill) statusPill.textContent = text;
  };

  const getSessionId = () => {
    let sid = localStorage.getItem(LS.SESSION);
    if (!sid) {
      sid = "s_" + Math.random().toString(36).slice(2, 10);
      localStorage.setItem(LS.SESSION, sid);
    }
    return sid;
  };

  const addMessage = (text, who) => {
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
    scrollToBottom();
    return msg;
  };

  const postJson = async (path, body) => {
    const res = await fetch(path, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });

    if (!res.ok) {
      return {
        messages: [{ text: "שגיאה בשרת או ברשת. נסה שוב." }],
        ui: {},
        data: {},
      };
    }

    const contentType = res.headers.get("content-type") || "";
    if (!contentType.includes("application/json")) {
      return {
        messages: [{ text: "השרת החזיר תשובה לא צפויה. נסה שוב." }],
        ui: {},
        data: {},
      };
    }

    return await res.json();
  };

  const saveSelectedStore = (store) => {
    localStorage.setItem(LS.STORE_ID, String(store.store_id));
    localStorage.setItem(LS.STORE_NAME, store.store_name);
  };

  const saveCouponCode = (code) => {
    if (code) localStorage.setItem(LS.COUPON_CODE, code);
    else localStorage.removeItem(LS.COUPON_CODE);
  };

  const showStores = (stores) => {
    if (!storeChips || !storesMessage) return;

    storeChips.innerHTML = "";

    stores.forEach((s) => {
      const btn = document.createElement("button");
      btn.className = "chip";
      btn.type = "button";
      btn.textContent = s.store_name;

      btn.addEventListener("click", async () => {
        const session_id = getSessionId();

        saveSelectedStore(s);
        addMessage(`בחרתי: ${s.store_name}`, "user");

        setStatus("שולח...");

        const resp = await postJson("/chat/store-click", {
          session_id,
          store_id: s.store_id,
        });

        (resp.messages || []).forEach((m) => addMessage(m.text, "bot"));

        renderCouponButtons(resp);
        setStatus("מוכן");
      });

      storeChips.appendChild(btn);
    });

    messages.appendChild(storesMessage);
    storesMessage.hidden = false;
    scrollToBottom();
  };

  const renderCouponButtons = (resp) => {
    if (!couponQuestion) return;

    const actions = qs(".actions", couponQuestion);
    if (!actions) return;

    actions.innerHTML = "";

    const buttons =
      resp?.ui?.coupon_buttons ?? [
        { answer: "yes", label: "כן" },
        { answer: "no", label: "לא" },
      ];

    buttons.forEach((b) => {
      const btn = document.createElement("button");
      btn.className = b.answer === "yes" ? "btn primary" : "btn secondary";
      btn.type = "button";
      btn.textContent = b.label;

      btn.addEventListener("click", async () => {
        const session_id = getSessionId();
        const store_id_str = localStorage.getItem(LS.STORE_ID);
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

        saveCouponCode(resp2?.data?.coupon_code || null);

        if (b.answer === "yes") window.location.href = "/coupon";
        else window.location.href = "/navigate";
      });

      actions.appendChild(btn);
    });

    messages.appendChild(couponQuestion);
    couponQuestion.hidden = false;
    scrollToBottom();
  };

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const text = input.value.trim();
    if (!text) return;

    if (storesMessage) storesMessage.hidden = true;
    if (couponQuestion) couponQuestion.hidden = true;

    addMessage(text, "user");
    input.value = "";

    const thinkingMsg = addMessage("מחפש... רגע", "bot");
    setStatus("מחפש...");

    const session_id = getSessionId();

    const resp = await postJson("/chat/message", {
      session_id,
      text,
      limit: 10,
    });

    if (thinkingMsg && thinkingMsg.parentNode) {
      thinkingMsg.parentNode.removeChild(thinkingMsg);
    }

    (resp.messages || []).forEach((m) => addMessage(m.text, "bot"));

    const stores = resp?.ui?.store_buttons ?? [];
    if (stores.length > 0) showStores(stores);

    setStatus("מוכן");
  });
})();
