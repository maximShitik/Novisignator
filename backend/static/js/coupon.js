const codeEl = document.getElementById("couponCode");
const storeEl = document.getElementById("couponStore");

const storeName = localStorage.getItem("sns_selected_store_name");
const couponCode = localStorage.getItem("sns_coupon_code");

if (storeEl && storeName) storeEl.textContent = storeName;
if (codeEl && couponCode) codeEl.textContent = couponCode;

if (codeEl && !couponCode) {
  codeEl.textContent = "אין קופון זמין";
}
