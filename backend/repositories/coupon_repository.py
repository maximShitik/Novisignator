from repositories.queries.coupon_queries import GET_BY_CODE, GET_BY_STORE
from infrastructure.logger import get_logger

logger = get_logger(__name__)

class CouponRepository:
    def __init__(self,db_pool):
        self.db_pool = db_pool


    def get_by_store(self,store_id):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(GET_BY_STORE, [store_id])
            coupons = cursor.fetchall()
            return coupons
        except Exception as e:
            logger.error(f"CouponRepository.get_by_store failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)


    def get_by_code(self, coupon_code):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(GET_BY_CODE, [coupon_code])
            coupon = cursor.fetchone()
            return coupon
        except Exception as e:
            logger.error(f"CouponRepository.get_by_code failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)


