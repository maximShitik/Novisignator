GET_BY_ID = "SELECT * FROM stores WHERE store_id = %s"
GET_BY_FLOOR = "SELECT * FROM stores WHERE floor = %s"
SEARCH = "SELECT * FROM stores WHERE store_name ILIKE %s OR category ILIKE %s"