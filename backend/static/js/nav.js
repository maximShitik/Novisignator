const img = document.getElementById("routeImg");
const title = document.getElementById("navTitle");

const storeId = localStorage.getItem("sns_selected_store_id");
const storeName = localStorage.getItem("sns_selected_store_name");

if (title && storeName) {
  title.textContent = `ניווט ל-${storeName}`;
}

async function loadRoute() {
  if (!storeId) return null;

  const res = await fetch(`/nav/route?store_id=${encodeURIComponent(storeId)}`);
  if (!res.ok) return null;

  const data = await res.json();
  return data.route_path_d || null; // <-- זה השדה הנכון אצלך
}

(async () => {
  if (!storeId || !img) return;

  const route = await loadRoute();
  if (!route) return;

  img.src = route;

  // אנימציה קטנה (אופציונלי)
  img.style.opacity = "0";
  img.style.transition = "opacity 250ms ease-in-out";
  requestAnimationFrame(() => {
    img.style.opacity = "1";
  });
})();
