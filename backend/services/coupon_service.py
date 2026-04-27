from infrastructure.logger import get_logger
logger = get_logger(__name__)

YES = { "success": True, "message": "Coupon claimed!" }
NO = { "success": False, "message": "Coupon not found" }
NO_COUPONS = { "success": False, "coupons": [] }


class CouponService():
    def __init__(self,coupon_repo,kafka_client):
        self.coupon_repo = coupon_repo
        self.kafka_client = kafka_client

    def display_coupons(self,store_id):
        coupons_list = []
        try:
            coupons = self.coupon_repo.get_by_store(store_id)

            if coupons:
                for coupon in coupons:
                    coupons_list.append({
                    "coupon_code": coupon[1],
                    "description": coupon[2]
                })
                return { "success": True, "coupons": coupons_list }
            else:
                return NO_COUPONS
        except Exception as e:
            logger.error(f"CouponService.display_coupons failed: {e}")
            raise
        

    def claim_coupon(self,coupon_code):
        try:
           coupon = self.coupon_repo.get_by_code(coupon_code)

           if coupon:
                topic = "mall.events.v1"
                message = {
                    "event": "COUPON_CLAIMED",
                    "coupon_code": coupon_code,
                    "store_id":coupon[0]}
                
                self.kafka_client.publish(topic, message)
                return YES
           else:
               return NO
        except Exception as e:
            logger.error(f"CouponService.claim_coupon failed: {e}")
            raise
        




