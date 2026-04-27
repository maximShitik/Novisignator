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
    <div>
      <h1>Coupons for {selectedStore.name}</h1>
      <div>
        {coupons.map((coupon, index) => {
         return <CouponCard
            key={index}
            couponCode={coupon.coupon_code}
            description={coupon.description}
            onClaim={handleClaim}
          />;
        })}
      </div>
      <button onClick={() => navigate("/navigate")}>
        Navigate to store
      </button>
    </div>
  );
};

export default CouponPage;
