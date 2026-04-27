const CouponCard = ({ couponCode, description, onClaim }) => {
  return(  <div>
    <h3>{couponCode}</h3>
    <p>{description}</p>
    <button onClick={() => onClaim(couponCode)}>Claim</button>
  </div>)

};

export default CouponCard;
