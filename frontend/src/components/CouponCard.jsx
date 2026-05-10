const CouponCard = ({ couponCode, description, onClaim }) => {
  return (
    <div  className="bg-white rounded-2xl border border-gray-200 p-4 flex flex-col gap-3">
      <p className="text-sm text-gray-600">{description}</p>
      <div className="bg-gray-100 rounded-xl p-3 text-lg font-semibold text-center">{couponCode}</div>
      
      <button onClick={() => onClaim(couponCode)} className="w-full h-10 px-6 rounded-xl bg-blue-600 flex items-center justify-center text-white hover:bg-blue-700 active:bg-blue-800 ">Claim</button>
    </div>
  );
};

export default CouponCard;
