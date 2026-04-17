from repositories.queries.navigation_queries import GET_SCAN_POINT_BY_ID, GET_NAVIGATION_ROUTE,GET_ALL_ROUTES
from infrastructure.logger import get_logger


logger = get_logger(__name__)
class NavigationRepository:
    def __init__(self,db_pool):
        self.db_pool = db_pool

    def get_scan_point_by_id(self,scan_point_id):
        conn = self.db_pool.getconn()
        try:
            cursor = conn.cursor()
            cursor.execute(GET_SCAN_POINT_BY_ID, [scan_point_id])
            scan_point = cursor.fetchone()
            return scan_point
        except Exception as e:
            logger.error(f"NavigationRepository.get_scan_point_by_id failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)

    def get_navigation_route(self,scan_point_id,store_id):
        conn = self.db_pool.getconn()
        try:
            cursor = conn.cursor()
            cursor.execute(GET_NAVIGATION_ROUTE, [store_id, scan_point_id])
            route = cursor.fetchone()
            return route
        except Exception as e:
            logger.error(f"NavigationRepository.get_navigation_route failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)



    def get_all_routes(self):
        conn = self.db_pool.getconn()
        try:
            cursor = conn.cursor()
            cursor.execute(GET_ALL_ROUTES)

            routes = cursor.fetchall()
            return routes
        except Exception as e:
            logger.error(f"NavigationRepository.get_all_routes failed: {e}")
            raise
        finally:
            self.db_pool.putconn(conn)

    