import { useEffect, useState } from "react";
import { getCurrentAd } from "../services/api";

const ScreenPage = () => {
  const [adUrl, setAdUrl] = useState(null);

  useEffect(() => {
    const getAd = async () => {
      const data = await getCurrentAd();
      setAdUrl(data.ad_url);
    };

    getAd();
    const timer = setInterval(getAd, 3000);

    return () => clearInterval(timer);
  }, []);

  return (
<div className="max-w-2xl w-full h-full flex flex-col bg-gray-900 shadow-lg rounded-xl overflow-hidden">    <div className="w-full h-full bg-gray-900 rounded-xl flex flex-col overflow-hidden">
      <div className="p-3 flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="w-2 h-2 rounded-full bg-green-500"></div>
          <p className="text-xs text-gray-400 tracking-widest">LIVE</p>
        </div>
        <p className="text-xs text-gray-600">Ads Display</p>
      </div>
      <div className="flex-1 flex items-center justify-center p-5">
        {adUrl ? (
          <img src={adUrl} className="max-w-full max-h-full rounded-xl" />
        ) : (
          <div className="text-center">
            <p className="text-gray-500 text-lg">Waiting for ad...</p>
            <p className="text-gray-600 text-xs mt-2">
              Ad will appear when a coupon is claimed
            </p>
          </div>
        )}
      </div>
      <div className="p-3 flex justify-between items-center">
        <p className="text-xs text-gray-600">Screen #1</p>
        <p className="text-xs text-gray-600">Polling every 3s</p>
      </div>
    </div>
    </div>
  );
};

export default ScreenPage;
