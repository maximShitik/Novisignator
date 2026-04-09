

SEARCH = "SELECT * FROM products WHERE product_name ILIKE %s OR category ILIKE %s"

GET_STORES_BY_PRODUCT = "SELECT stores.store_id, stores.store_name FROM stores JOIN store_products ON stores.store_id = store_products.store_id  WHERE store_products.product_id = %s  "