(() => {
  const codeEl = document.getElementById("couponCode");
  const storeEl = document.getElementById("couponStore");
  if (!codeEl && !storeEl) return;

  const LS = {
    STORE_NAME: "sns_selected_store_name",
    COUPON_CODE: "sns_coupon_code",
  };

  const storeName = localStorage.getItem(LS.STORE_NAME);
  const couponCode = localStorage.getItem(LS.COUPON_CODE);

  if (storeEl) storeEl.textContent = storeName || "לא נבחרה חנות";
  if (codeEl) codeEl.textContent = couponCode || "אין קופון זמין";
})();
