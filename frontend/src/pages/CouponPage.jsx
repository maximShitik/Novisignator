import { useEffect, useState } from "react";
import { useApp } from "../context/AppContext";
import { displayCoupons, claimCoupon } from "../services/api";
import CouponCard from "../components/CouponCard";
import { useNavigate } from "react-router-dom"

const CouponPage = () => {
  const { selectedStore } = useApp();
  const [coupons, setCoupons] = useState([]);
  const navigate = useNavigate()


  useEffect(() => {
    const fetchCoupons = async () => {
      const data = await displayCoupons(selectedStore.id);
      setCoupons(data);
    };
    fetchCoupons();
  }, []);

  const handleClaim = async (couponCode) => {
    await claimCoupon(couponCode);
  };



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
