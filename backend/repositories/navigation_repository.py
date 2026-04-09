from repositories.queries.navigation_queries import GET_SCAN_POINT_BY_ID, GET_NAVIGATION_ROUTE

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
            raise Exception(f"NavigationRepository.get_scan_point_by_id failed: {e}")
        finally:
            self.db_pool.putconn(conn)

    def get_navigation_route(self,store_id,scan_point_id):
        conn = self.db_pool.getconn()
        try:
            cursor = conn.cursor()
            cursor.execute(GET_NAVIGATION_ROUTE, [store_id, scan_point_id]
)
            route = cursor.fetchone()
            return route
        except Exception as e:
            raise Exception(f"NavigationRepository.get_navigation_route failed: {e}")
        finally:
            self.db_pool.putconn(conn)


    

