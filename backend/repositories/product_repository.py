from repositories.queries.product_queries import GET_STORES_BY_PRODUCT , SEARCH
from infrastructure.logger import get_logger
logger = get_logger(__name__)

class ProductRepository:
    def __init__(self,db_pool):
        self.db_pool = db_pool
    
    # returns what products are exsits
    def search(self, query):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(SEARCH, [f"%{query}%", f"%{query}%"])
            store = cursor.fetchall()
            return store
        except Exception as e:
            logger.error(f"ProductRepository.search failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)

    # returns the stores that sell the products, can be called after search
    def get_stores_by_product(self,product_id):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(GET_STORES_BY_PRODUCT,[product_id])
            store = cursor.fetchall()
            return store
        except Exception as e:
            logger.error(f"ProductRepository.get_stores_by_product failed: {e}")
            raise

        finally:
            self.db_pool.putconn(conn)



