from repositories.queries.store_queries import GET_BY_FLOOR , GET_BY_ID , SEARCH
from infrastructure.logger import get_logger


logger = get_logger(__name__)

class StoreRepository:
    def __init__(self, db_pool):
        self.db_pool =  db_pool

    def get_by_id(self, store_id):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(GET_BY_ID, [store_id])
            store = cursor.fetchone()
            return store
        except Exception as e:
            logger.error(f"StoreRepository.get_by_id failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)

    def get_by_floor(self, floor):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(GET_BY_FLOOR, [floor])
            stores = cursor.fetchall()
            return stores
        except Exception as e:
            logger.error(f"StoreRepository.get_by_floor failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)


    
    def search(self, query):
        conn = self.db_pool.getconn()

        try:
            cursor = conn.cursor()
            cursor.execute(SEARCH, [f"%{query}%", f"%{query}%"])
            results = cursor.fetchall()
            return results
        except Exception as e:
            logger.error(f"StoreRepository.search failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)
