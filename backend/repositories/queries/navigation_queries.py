
GET_SCAN_POINT_BY_ID = "SELECT * FROM scan_points WHERE scan_point_id = %s"

GET_NAVIGATION_ROUTE = "SELECT * FROM store_navigation WHERE store_id=%s and scan_point_id=%s "

GET_ALL_ROUTES = "SELECT * FROM store_navigation "