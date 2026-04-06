

class CouponService():
    def __init__(self,coupon_repo,kafka_client):
        self.coupon_repo = coupon_repo
        self.kafka_client = kafka_client

    def display_coupons(self,store_id): pass

    def claim_coupon(self,coupon_code): pass