GET_STORES = """
SELECT store_id, store_name
FROM stores
ORDER BY store_id ASC;
"""

GET_STORE_BY_ID = """
SELECT store_id, store_name
FROM stores
WHERE store_id = ?;
"""


SEARCH_PRODUCTS = """
SELECT
  p.product_id,
  p.product_name,
  p.category,
  s.store_id,
  s.store_name
FROM products p
JOIN stores s ON s.store_id = p.store_id
WHERE
  LOWER(p.product_name) LIKE LOWER(?) OR
  LOWER(p.category) LIKE LOWER(?) OR
  LOWER(s.store_name) LIKE LOWER(?)
ORDER BY s.store_id, p.product_name
LIMIT ?;
"""

GET_PRODUCTS_BY_STORE = """
SELECT
  product_id, product_name, category
FROM products
WHERE store_id = ?
ORDER BY product_name ASC;
"""

GET_NAVIGATION_ASSET_BY_STORE = """
SELECT
  s.store_id,
  s.store_name,
  n.map_target_id,
  n.route_path_d
FROM stores s
JOIN store_navigation n ON n.store_id = s.store_id
WHERE s.store_id = ?;
"""


GET_COUPON_BY_STORE = """
SELECT store_id, coupon_code
FROM coupons
WHERE store_id = ?;
"""

GET_COUPON_BY_PRODUCT = """
SELECT c.store_id, c.coupon_code
FROM products p
JOIN coupons c ON c.store_id = p.store_id
WHERE p.product_id = ?;
"""

GET_ALL_ADS = """
SELECT
  ad_id,
  store_id,
  ad_type,
  asset_url,
  trigger,
  is_active,
  created_at
FROM ads
ORDER BY ad_id DESC;
"""

GET_DEFAULT_AD_BY_STORE = """
SELECT ad_id, ad_type, asset_url
FROM ads
WHERE store_id = ?
  AND trigger = 'default'
  AND is_active = 1
ORDER BY ad_id DESC
LIMIT 1;
"""

GET_COUPON_YES_AD_BY_STORE = """
SELECT ad_id, ad_type, asset_url
FROM ads
WHERE store_id = ?
  AND trigger = 'coupon_yes'
  AND is_active = 1
ORDER BY ad_id DESC
LIMIT 1;
"""

GET_BEST_AD_BY_STORE = """
SELECT ad_id, ad_type, asset_url, trigger
FROM ads
WHERE store_id = ?
  AND is_active = 1
  AND trigger IN ('coupon_yes', 'default')
ORDER BY CASE trigger
  WHEN 'coupon_yes' THEN 0
  ELSE 1
END,
ad_id DESC
LIMIT 1;
"""

DISABLE_AD_BY_ID = """
UPDATE ads
SET is_active = 0
WHERE ad_id = ?;
"""

DELETE_AD_BY_ID = """
DELETE FROM ads
WHERE ad_id = ?;
"""

GET_ROUTE_BY_STORE = """
SELECT store_id, map_target_id, route_path_d
FROM store_navigation
WHERE store_id = ?;
"""

GET_SUGGESTIONS = """
SELECT DISTINCT term FROM (
  SELECT product_name AS term FROM products
  UNION
  SELECT category AS term FROM products
  UNION
  SELECT store_name AS term FROM stores
)
WHERE LOWER(term) LIKE LOWER(?)
LIMIT ?;
"""
