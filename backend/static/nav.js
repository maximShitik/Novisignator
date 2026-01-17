const path = document.getElementById("routePath");
const title = document.getElementById("navTitle");

const storeId = localStorage.getItem("sns_selected_store_id");
const storeName = localStorage.getItem("sns_selected_store_name");

if (title && storeName) {
  title.textContent = `ניווט ל-${storeName}`;
}

function preparePath() {
  const length = path.getTotalLength();
  path.style.strokeDasharray = length;
  path.style.strokeDashoffset = length;
  path.style.transition = "none";
}

function play(durationMs = 1300) {
  path.style.transition = `stroke-dashoffset ${durationMs}ms ease-in-out`;
  requestAnimationFrame(() => {
    path.style.strokeDashoffset = "0";
  });
}

async function loadRouteD() {
  if (!storeId) return null;

  const res = await fetch(`/nav/route?store_id=${encodeURIComponent(storeId)}`);
  if (!res.ok) return null;

  const data = await res.json();
  return data.route_path_d || null;
}

(async () => {
  // אם אין חנות נבחרת — אפשר להחזיר לצ'אט
  if (!storeId) {
    // window.location.href = "/";
    return;
  }

  const d = await loadRouteD();
  if (!d) {
    // fallback: אל תאנימציה אם אין נתיב
    return;
  }

  // לשבץ את הנתיב של החנות שנבחרה
  path.setAttribute("d", d);

  // ואז האנימציה
  preparePath();
  play(1400);
})();
