import { useEffect, useState } from "react";
import { useApp } from "../context/AppContext";
import { displayCoupons, claimCoupon } from "../services/api";
import CouponCard from "../components/CouponCard";
import { useNavigate } from "react-router-dom"

const CouponPage = () => {
  const { selectedStore } = useApp();
  console.log("COUPON PAGE - selectedStore:", selectedStore)
  const [coupons, setCoupons] = useState([]);
  const navigate = useNavigate()


  useEffect(() => {
    if (!selectedStore) return
    const fetchCoupons = async () => {
      const data = await displayCoupons(selectedStore.id);
      console.log("COUPONS DATA:", data.coupons)

      setCoupons(data.coupons);
    };
    fetchCoupons();
  }, []);


  const handleClaim = async (couponCode) => {
    await claimCoupon(couponCode);
  };

  if (!selectedStore) {
    return <p>No store selected. Go back to chat.</p>
  }


  return (
    <div className="max-w-lg w-full h-full flex flex-col  bg-white shadow-lg rounded-xl overflow-hidden "
      >
      <div className="p-4 border-b flex justify-between items-center">
        <div className="flex items-center gap-2">
          <div className="w-9 h-9 rounded-full bg-blue-600 flex items-center justify-center text-white">
            N
          </div>
          <div>
            <h1 className="text-lg font-semibold"> Coupons -  {selectedStore.name}</h1>
            <p className="text-xs text-gray-500">
             Choose a coupon
            </p>
          </div>
        </div>
        <button onClick={() => navigate("/")} className="bg-gray-200 text-gray-600 px-2 py-1 rounded-full hover:bg-gray-300 active:bg-gray-300">חזרה</button>

      </div>

      <div className="flex-1 overflow-y-auto p-4 flex flex-col gap-4 bg-gray-50">
        {coupons.map((coupon, index) => {
          return <CouponCard
            key={index}
            couponCode={coupon.coupon_code}
            description={coupon.description}
            onClaim={handleClaim}
          />;
        })}
      </div>
      <div className="p-4 border-t">
        <button onClick={() => navigate("/navigate")} className="w-full h-12 rounded-xl bg-gray-100 text-gray-800 border border-gray-300 flex items-center justify-center hover:bg-gray-200 active:bg-gray-300">
         Navigate to store
        </button>
      </div>
    </div>
  );
};

export default CouponPage;
