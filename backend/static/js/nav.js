(() => {
  const img = document.getElementById("routeImg");
  const title = document.getElementById("navTitle");
  if (!img && !title) return;

  const LS = {
    STORE_ID: "sns_selected_store_id",
    STORE_NAME: "sns_selected_store_name",
  };

  const storeId = localStorage.getItem(LS.STORE_ID);
  const storeName = localStorage.getItem(LS.STORE_NAME);

  if (title) title.textContent = storeName ? `ניווט ל-${storeName}` : "ניווט";

  const loadRoute = async () => {
    if (!storeId) return null;

    const res = await fetch(`/nav/route?store_id=${encodeURIComponent(storeId)}`);
    if (!res.ok) return null;

    const contentType = res.headers.get("content-type") || "";
    if (!contentType.includes("application/json")) return null;

    const data = await res.json();
    return data?.route_path_d || null;
  };

  (async () => {
    if (!storeId || !img) return;

    const route = await loadRoute();
    if (!route) return;

    img.src = route;

    img.style.opacity = "0";
    img.style.transition = "opacity 250ms ease-in-out";
    requestAnimationFrame(() => (img.style.opacity = "1"));
  })();
})();
