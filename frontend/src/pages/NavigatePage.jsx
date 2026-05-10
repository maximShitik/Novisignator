import { useEffect, useState } from "react";
import { useApp } from "../context/AppContext";
import { getRoute } from "../services/api";
import MapView from "../components/MapView";
import { useNavigate } from "react-router-dom";

const NavigatePage = () => {
  const { selectedStore, scanPointId } = useApp();
  const [routePath, setRoutePath] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    if (!selectedStore || !scanPointId) return;
    const fetchRoute = async () => {
      const data = await getRoute(scanPointId, selectedStore.id);
      setRoutePath(data.route);
    };
    fetchRoute();
  }, []);

  if (!selectedStore || !scanPointId) {
    return <p>No store or scan point selected. Go back to chat.</p>;
  }

  return (
    <div className="max-w-lg w-full h-full flex flex-col bg-white shadow-lg rounded-xl overflow-hidden ">
      <div className="p-4 border-b flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="w-9 h-9 rounded-full bg-blue-600 flex items-center justify-center text-white">
            N
          </div>
          <div>
            <h1 className="text-lg font-semibold">
              Navigate - {selectedStore.name}
            </h1>
            <p className="text-xs text-gray-500">Navigation</p>
          </div>
        </div>
        <button
          onClick={() => navigate("/")}
          className="bg-gray-200 text-gray-600 px-2 py-1 rounded-full hover:bg-gray-300 active:bg-gray-300"
        >
          Back
        </button>
      </div>

      <div className="flex-1 overflow-y-auto p-4 bg-gray-50">
        <div className="bg-white rounded-2xl border border-gray-200 h-full flex items-center justify-center">
          <MapView routePath={routePath} />
        </div>
      </div>

      <div className="p-4 border-t flex gap-2">
        {selectedStore.id && (
          <button onClick={() => navigate("/coupon")} className="flex-1 h-12 rounded-xl bg-blue-600 text-white flex items-center justify-center hover:bg-blue-700 active:bg-blue-800">Coupons</button>
        )}
        <button onClick={() => navigate("/")} className="flex-1 h-12 rounded-xl bg-gray-100 text-gray-800 border border-gray-300 flex items-center justify-center hover:bg-gray-400 active:bg-gray-400">Back to chat</button>
      </div>
    </div>
  );
};

export default NavigatePage;
