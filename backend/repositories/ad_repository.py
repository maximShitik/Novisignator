from repositories.queries.ad_queries import GET_AD_BY_STORE_ID
from infrastructure.logger import get_logger
logger = get_logger(__name__)

class AdRepository:
    def __init__(self, db_pool):
        self.db_pool =  db_pool

    def get_ad_by_store_id(self,store_id):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(GET_AD_BY_STORE_ID,[store_id])
            ad = cursor.fetchone()
            return ad
        except Exception as e:
            logger.error(f"AdRepository.get_ad_by_store_id failed: {e}")
            raise

        finally:
            self.db_pool.putconn(conn)

