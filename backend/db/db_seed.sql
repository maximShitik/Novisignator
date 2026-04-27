-- ============================================
-- NoviSignator — Azrieli Mall Tel Aviv Seed Data
-- ============================================

-- Clear existing data (order matters for foreign keys)
DELETE FROM ads;
DELETE FROM store_navigation;
DELETE FROM coupons;
DELETE FROM store_products;
DELETE FROM products;
DELETE FROM scan_points;
DELETE FROM stores;

-- ============================================
-- STORES (30 stores across 3 floors)
-- ============================================

-- Floor 1 — Fashion & Shoes
INSERT INTO stores (store_id, store_name, category, floor) OVERRIDING SYSTEM VALUE VALUES
(1, 'Zara', 'Fashion', 1),
(2, 'H&M', 'Fashion', 1),
(3, 'Castro', 'Fashion', 1),
(4, 'American Eagle', 'Fashion', 1),
(5, 'Adidas', 'Fashion', 1),
(6, 'Bershka', 'Fashion', 1),
(7, 'ALDO', 'Shoes', 1),
(8, 'Steve Madden', 'Shoes', 1),
(9, 'Black & White', 'Shoes', 1),
(10, '& Other Stories', 'Fashion', 1);

-- Floor 2 — Electronics, Cosmetics, Accessories
INSERT INTO stores (store_id, store_name, category, floor) OVERRIDING SYSTEM VALUE VALUES
(11, 'Bug', 'Electronics', 2),
(12, 'iDigital', 'Electronics', 2),
(13, 'Bobby Brown', 'Cosmetics', 2),
(14, 'Carolina Lemke', 'Optics', 2),
(15, 'Pandora', 'Jewelry', 2),
(16, 'Asaf & Tomer', 'Jewelry', 2),
(17, 'Billabong', 'Fashion', 2),
(18, 'AERIE', 'Fashion', 2),
(19, 'Diesel', 'Fashion', 2),
(20, 'GAP', 'Fashion', 2);

-- Floor 3 — Food & Beverages
INSERT INTO stores (store_id, store_name, category, floor) OVERRIDING SYSTEM VALUE VALUES
(21, 'Aroma', 'Food & Beverages', 3),
(22, 'Arcaffe', 'Food & Beverages', 3),
(23, 'Burger King', 'Food & Beverages', 3),
(24, 'Burgers Bar', 'Food & Beverages', 3),
(25, 'Abulafia', 'Food & Beverages', 3),
(26, 'B-Fresh', 'Food & Beverages', 3),
(27, 'Black Burger', 'Food & Beverages', 3),
(28, 'Broaster Chicken', 'Food & Beverages', 3),
(29, 'Cafe Cafe', 'Food & Beverages', 3),
(30, 'Candy World', 'Food & Beverages', 3);

-- Reset the sequence so next auto-generated ID starts after 30
SELECT setval(pg_get_serial_sequence('stores', 'store_id'), 30);

-- ============================================
-- PRODUCTS (35 products)
-- ============================================
INSERT INTO products (product_id, product_name, category) OVERRIDING SYSTEM VALUE VALUES
-- Clothing
(1, 'חולצת טי', 'Clothing'),
(2, 'ג׳ינס', 'Clothing'),
(3, 'שמלה', 'Clothing'),
(4, 'חצאית', 'Clothing'),
(5, 'מעיל', 'Clothing'),
(6, 'סווטשירט', 'Clothing'),
(7, 'מכנסי ספורט', 'Clothing'),
(8, 'חולצה מכופתרת', 'Clothing'),
-- Shoes
(9, 'נעלי ספורט', 'Shoes'),
(10, 'סנדלים', 'Shoes'),
(11, 'מגפיים', 'Shoes'),
(12, 'נעלי עקב', 'Shoes'),
(13, 'כפכפים', 'Shoes'),
-- Electronics
(14, 'אוזניות', 'Electronics'),
(15, 'מטען', 'Electronics'),
(16, 'כיסוי לטלפון', 'Electronics'),
(17, 'רמקול בלוטוס', 'Electronics'),
(18, 'שעון חכם', 'Electronics'),
-- Cosmetics
(19, 'שפתון', 'Cosmetics'),
(20, 'קרם פנים', 'Cosmetics'),
(21, 'בושם', 'Cosmetics'),
(22, 'מסקרה', 'Cosmetics'),
-- Accessories
(23, 'משקפי שמש', 'Accessories'),
(24, 'צמיד', 'Accessories'),
(25, 'שרשרת', 'Accessories'),
(26, 'טבעת', 'Accessories'),
(27, 'תיק יד', 'Accessories'),
-- Food
(28, 'קפה', 'Food'),
(29, 'עוגה', 'Food'),
(30, 'המבורגר', 'Food'),
(31, 'פיצה', 'Food'),
(32, 'סלט', 'Food'),
(33, 'שייק', 'Food'),
(34, 'לחמניה', 'Food'),
(35, 'כנפיים', 'Food');

-- Reset the sequence
SELECT setval(pg_get_serial_sequence('products', 'product_id'), 35);

-- ============================================
-- STORE_PRODUCTS (which stores sell which products)
-- ============================================
INSERT INTO store_products (store_id, product_id) VALUES
-- Zara
(1, 1), (1, 2), (1, 3), (1, 4), (1, 5),
-- H&M
(2, 1), (2, 2), (2, 3), (2, 5), (2, 6),
-- Castro
(3, 1), (3, 2), (3, 3), (3, 8),
-- American Eagle
(4, 1), (4, 2), (4, 6), (4, 7),
-- Adidas
(5, 1), (5, 7), (5, 9), (5, 6),
-- Bershka
(6, 1), (6, 2), (6, 3), (6, 4),
-- ALDO
(7, 9), (7, 10), (7, 11), (7, 12), (7, 27),
-- Steve Madden
(8, 9), (8, 11), (8, 12), (8, 27),
-- Black & White
(9, 9), (9, 10), (9, 11), (9, 13),
-- & Other Stories
(10, 3), (10, 19), (10, 21), (10, 27),
-- Bug
(11, 14), (11, 15), (11, 16), (11, 17), (11, 18),
-- iDigital
(12, 14), (12, 15), (12, 16), (12, 17), (12, 18),
-- Bobby Brown
(13, 19), (13, 20), (13, 21), (13, 22),
-- Carolina Lemke
(14, 23),
-- Pandora
(15, 24), (15, 25), (15, 26),
-- Asaf & Tomer
(16, 24), (16, 25), (16, 26),
-- Billabong
(17, 1), (17, 7), (17, 9), (17, 13),
-- AERIE
(18, 1), (18, 6),
-- Diesel
(19, 1), (19, 2), (19, 5), (19, 27),
-- GAP
(20, 1), (20, 2), (20, 6), (20, 7),
-- Aroma
(21, 28), (21, 29), (21, 32),
-- Arcaffe
(22, 28), (22, 29), (22, 32),
-- Burger King
(23, 30), (23, 33),
-- Burgers Bar
(24, 30), (24, 35), (24, 33),
-- Abulafia
(25, 31), (25, 34),
-- B-Fresh
(26, 32), (26, 33),
-- Black Burger
(27, 30), (27, 35),
-- Broaster Chicken
(28, 35), (28, 32),
-- Cafe Cafe
(29, 28), (29, 29), (29, 32),
-- Candy World
(30, 29);

-- ============================================
-- SCAN POINTS (5 locations in the mall)
-- ============================================
INSERT INTO scan_points (scan_point_id, scan_point_name) OVERRIDING SYSTEM VALUE VALUES
(1, 'כניסה ראשית'),
(2, 'כניסה מהרכבת'),
(3, 'קומה 1 - מרכז'),
(4, 'קומה 2 - מרכז'),
(5, 'קומה 3 - אזור אוכל');

-- Reset the sequence
SELECT setval(pg_get_serial_sequence('scan_points', 'scan_point_id'), 5);

-- ============================================
-- STORE NAVIGATION (5 scan points × 30 stores = 150 routes)
-- ============================================

-- From Scan Point 1 (Main Entrance)
INSERT INTO store_navigation (store_id, scan_point_id, route_path_d) VALUES
(1, 1, 'M 50 400 L 150 400 L 150 300'),
(2, 1, 'M 50 400 L 200 400 L 200 350'),
(3, 1, 'M 50 400 L 100 400 L 100 250'),
(4, 1, 'M 50 400 L 250 400 L 250 300'),
(5, 1, 'M 50 400 L 300 400 L 300 350'),
(6, 1, 'M 50 400 L 350 400 L 350 300'),
(7, 1, 'M 50 400 L 150 400 L 150 200'),
(8, 1, 'M 50 400 L 200 400 L 200 200'),
(9, 1, 'M 50 400 L 250 400 L 250 200'),
(10, 1, 'M 50 400 L 400 400 L 400 300'),
(11, 1, 'M 50 400 L 50 300 L 150 300 L 150 200'),
(12, 1, 'M 50 400 L 50 300 L 200 300 L 200 200'),
(13, 1, 'M 50 400 L 50 300 L 100 300 L 100 200'),
(14, 1, 'M 50 400 L 50 300 L 250 300 L 250 200'),
(15, 1, 'M 50 400 L 50 300 L 300 300 L 300 200'),
(16, 1, 'M 50 400 L 50 300 L 350 300 L 350 200'),
(17, 1, 'M 50 400 L 50 300 L 150 300 L 150 150'),
(18, 1, 'M 50 400 L 50 300 L 200 300 L 200 150'),
(19, 1, 'M 50 400 L 50 300 L 250 300 L 250 150'),
(20, 1, 'M 50 400 L 50 300 L 400 300 L 400 200'),
(21, 1, 'M 50 400 L 50 200 L 150 200 L 150 100'),
(22, 1, 'M 50 400 L 50 200 L 200 200 L 200 100'),
(23, 1, 'M 50 400 L 50 200 L 100 200 L 100 100'),
(24, 1, 'M 50 400 L 50 200 L 250 200 L 250 100'),
(25, 1, 'M 50 400 L 50 200 L 300 200 L 300 100'),
(26, 1, 'M 50 400 L 50 200 L 350 200 L 350 100'),
(27, 1, 'M 50 400 L 50 200 L 150 200 L 150 50'),
(28, 1, 'M 50 400 L 50 200 L 200 200 L 200 50'),
(29, 1, 'M 50 400 L 50 200 L 250 200 L 250 50'),
(30, 1, 'M 50 400 L 50 200 L 400 200 L 400 100');

-- From Scan Point 2 (Train Station Entrance)
INSERT INTO store_navigation (store_id, scan_point_id, route_path_d) VALUES
(1, 2, 'M 450 400 L 350 400 L 150 300'),
(2, 2, 'M 450 400 L 350 400 L 200 350'),
(3, 2, 'M 450 400 L 350 400 L 100 250'),
(4, 2, 'M 450 400 L 350 400 L 250 300'),
(5, 2, 'M 450 400 L 350 400 L 300 350'),
(6, 2, 'M 450 400 L 350 400 L 350 300'),
(7, 2, 'M 450 400 L 350 400 L 150 200'),
(8, 2, 'M 450 400 L 350 400 L 200 200'),
(9, 2, 'M 450 400 L 350 400 L 250 200'),
(10, 2, 'M 450 400 L 350 400 L 400 300'),
(11, 2, 'M 450 400 L 450 300 L 150 200'),
(12, 2, 'M 450 400 L 450 300 L 200 200'),
(13, 2, 'M 450 400 L 450 300 L 100 200'),
(14, 2, 'M 450 400 L 450 300 L 250 200'),
(15, 2, 'M 450 400 L 450 300 L 300 200'),
(16, 2, 'M 450 400 L 450 300 L 350 200'),
(17, 2, 'M 450 400 L 450 300 L 150 150'),
(18, 2, 'M 450 400 L 450 300 L 200 150'),
(19, 2, 'M 450 400 L 450 300 L 250 150'),
(20, 2, 'M 450 400 L 450 300 L 400 200'),
(21, 2, 'M 450 400 L 450 200 L 150 100'),
(22, 2, 'M 450 400 L 450 200 L 200 100'),
(23, 2, 'M 450 400 L 450 200 L 100 100'),
(24, 2, 'M 450 400 L 450 200 L 250 100'),
(25, 2, 'M 450 400 L 450 200 L 300 100'),
(26, 2, 'M 450 400 L 450 200 L 350 100'),
(27, 2, 'M 450 400 L 450 200 L 150 50'),
(28, 2, 'M 450 400 L 450 200 L 200 50'),
(29, 2, 'M 450 400 L 450 200 L 250 50'),
(30, 2, 'M 450 400 L 450 200 L 400 100');

-- From Scan Point 3 (Floor 1 Center)
INSERT INTO store_navigation (store_id, scan_point_id, route_path_d) VALUES
(1, 3, 'M 250 350 L 150 300'),
(2, 3, 'M 250 350 L 200 350'),
(3, 3, 'M 250 350 L 100 250'),
(4, 3, 'M 250 350 L 250 300'),
(5, 3, 'M 250 350 L 300 350'),
(6, 3, 'M 250 350 L 350 300'),
(7, 3, 'M 250 350 L 150 200'),
(8, 3, 'M 250 350 L 200 200'),
(9, 3, 'M 250 350 L 250 200'),
(10, 3, 'M 250 350 L 400 300'),
(11, 3, 'M 250 350 L 250 250 L 150 200'),
(12, 3, 'M 250 350 L 250 250 L 200 200'),
(13, 3, 'M 250 350 L 250 250 L 100 200'),
(14, 3, 'M 250 350 L 250 250 L 250 200'),
(15, 3, 'M 250 350 L 250 250 L 300 200'),
(16, 3, 'M 250 350 L 250 250 L 350 200'),
(17, 3, 'M 250 350 L 250 250 L 150 150'),
(18, 3, 'M 250 350 L 250 250 L 200 150'),
(19, 3, 'M 250 350 L 250 250 L 250 150'),
(20, 3, 'M 250 350 L 250 250 L 400 200'),
(21, 3, 'M 250 350 L 250 150 L 150 100'),
(22, 3, 'M 250 350 L 250 150 L 200 100'),
(23, 3, 'M 250 350 L 250 150 L 100 100'),
(24, 3, 'M 250 350 L 250 150 L 250 100'),
(25, 3, 'M 250 350 L 250 150 L 300 100'),
(26, 3, 'M 250 350 L 250 150 L 350 100'),
(27, 3, 'M 250 350 L 250 150 L 150 50'),
(28, 3, 'M 250 350 L 250 150 L 200 50'),
(29, 3, 'M 250 350 L 250 150 L 250 50'),
(30, 3, 'M 250 350 L 250 150 L 400 100');

-- From Scan Point 4 (Floor 2 Center)
INSERT INTO store_navigation (store_id, scan_point_id, route_path_d) VALUES
(1, 4, 'M 250 250 L 250 350 L 150 300'),
(2, 4, 'M 250 250 L 250 350 L 200 350'),
(3, 4, 'M 250 250 L 250 350 L 100 250'),
(4, 4, 'M 250 250 L 250 350 L 250 300'),
(5, 4, 'M 250 250 L 250 350 L 300 350'),
(6, 4, 'M 250 250 L 250 350 L 350 300'),
(7, 4, 'M 250 250 L 250 350 L 150 200'),
(8, 4, 'M 250 250 L 250 350 L 200 200'),
(9, 4, 'M 250 250 L 250 350 L 250 200'),
(10, 4, 'M 250 250 L 250 350 L 400 300'),
(11, 4, 'M 250 250 L 150 200'),
(12, 4, 'M 250 250 L 200 200'),
(13, 4, 'M 250 250 L 100 200'),
(14, 4, 'M 250 250 L 250 200'),
(15, 4, 'M 250 250 L 300 200'),
(16, 4, 'M 250 250 L 350 200'),
(17, 4, 'M 250 250 L 150 150'),
(18, 4, 'M 250 250 L 200 150'),
(19, 4, 'M 250 250 L 250 150'),
(20, 4, 'M 250 250 L 400 200'),
(21, 4, 'M 250 250 L 250 150 L 150 100'),
(22, 4, 'M 250 250 L 250 150 L 200 100'),
(23, 4, 'M 250 250 L 250 150 L 100 100'),
(24, 4, 'M 250 250 L 250 150 L 250 100'),
(25, 4, 'M 250 250 L 250 150 L 300 100'),
(26, 4, 'M 250 250 L 250 150 L 350 100'),
(27, 4, 'M 250 250 L 250 150 L 150 50'),
(28, 4, 'M 250 250 L 250 150 L 200 50'),
(29, 4, 'M 250 250 L 250 150 L 250 50'),
(30, 4, 'M 250 250 L 250 150 L 400 100');

-- From Scan Point 5 (Floor 3 Food Court)
INSERT INTO store_navigation (store_id, scan_point_id, route_path_d) VALUES
(1, 5, 'M 250 100 L 250 350 L 150 300'),
(2, 5, 'M 250 100 L 250 350 L 200 350'),
(3, 5, 'M 250 100 L 250 350 L 100 250'),
(4, 5, 'M 250 100 L 250 350 L 250 300'),
(5, 5, 'M 250 100 L 250 350 L 300 350'),
(6, 5, 'M 250 100 L 250 350 L 350 300'),
(7, 5, 'M 250 100 L 250 350 L 150 200'),
(8, 5, 'M 250 100 L 250 350 L 200 200'),
(9, 5, 'M 250 100 L 250 350 L 250 200'),
(10, 5, 'M 250 100 L 250 350 L 400 300'),
(11, 5, 'M 250 100 L 250 250 L 150 200'),
(12, 5, 'M 250 100 L 250 250 L 200 200'),
(13, 5, 'M 250 100 L 250 250 L 100 200'),
(14, 5, 'M 250 100 L 250 250 L 250 200'),
(15, 5, 'M 250 100 L 250 250 L 300 200'),
(16, 5, 'M 250 100 L 250 250 L 350 200'),
(17, 5, 'M 250 100 L 250 250 L 150 150'),
(18, 5, 'M 250 100 L 250 250 L 200 150'),
(19, 5, 'M 250 100 L 250 250 L 250 150'),
(20, 5, 'M 250 100 L 250 250 L 400 200'),
(21, 5, 'M 250 100 L 150 100'),
(22, 5, 'M 250 100 L 200 100'),
(23, 5, 'M 250 100 L 100 100'),
(24, 5, 'M 250 100 L 250 100'),
(25, 5, 'M 250 100 L 300 100'),
(26, 5, 'M 250 100 L 350 100'),
(27, 5, 'M 250 100 L 150 50'),
(28, 5, 'M 250 100 L 200 50'),
(29, 5, 'M 250 100 L 250 50'),
(30, 5, 'M 250 100 L 400 100');

-- ============================================
-- COUPONS (realistic discounts in Hebrew)
-- ============================================
INSERT INTO coupons (store_id, coupon_code, description) VALUES
(1, 'ZARA20', '20% הנחה על כל הקולקציה'),
(1, 'ZARA50', '50 ש״ח הנחה בקנייה מעל 300'),
(2, 'HM15', '15% הנחה על פריט שני'),
(3, 'CASTRO30', '30% הנחה על מכנסיים'),
(4, 'AE25', '25% הנחה על חולצות'),
(5, 'ADIDAS40', '40% הנחה על נעלי ספורט'),
(5, 'ADIDAS20', '20% הנחה על ביגוד ספורט'),
(6, 'BERSHKA10', '10% הנחה על כל החנות'),
(7, 'ALDO30', '30% הנחה על תיקים'),
(8, 'STEVE25', '25% הנחה על מגפיים'),
(11, 'BUG50', '50 ש״ח הנחה על אוזניות'),
(12, 'IDIG100', '100 ש״ח הנחה על שעון חכם'),
(13, 'BOBBY20', '20% הנחה על בשמים'),
(14, 'LEMKE30', '30% הנחה על משקפי שמש'),
(15, 'PANDORA15', '15% הנחה על צמידים'),
(19, 'DIESEL20', '20% הנחה על ג׳ינסים'),
(20, 'GAP25', '25% הנחה על סווטשירטים'),
(21, 'AROMA10', 'מאפה חינם עם כל קפה'),
(22, 'ARCAFFE15', '15% הנחה על ארוחת בוקר'),
(23, 'BK20', '20% הנחה על ארוחה'),
(24, 'BURGER25', '25% הנחה על המבורגר');

-- ============================================
-- ADS (promotional content for digital signage)
-- trig must be 'default' or 'coupon_yes'
-- ad_type must be 'image' or 'navigation'
-- ============================================
INSERT INTO ads (store_id, ad_type, asset_url, trig, is_active) VALUES
(1, 'image', 'https://s3.amazonaws.com/novisignator/ads/zara_summer.jpg', 'coupon_yes', true),
(2, 'image', 'https://s3.amazonaws.com/novisignator/ads/hm_sale.jpg', 'coupon_yes', true),
(3, 'image', 'https://s3.amazonaws.com/novisignator/ads/castro_new.jpg', 'coupon_yes', true),
(5, 'image', 'https://s3.amazonaws.com/novisignator/ads/adidas_sport.jpg', 'coupon_yes', true),
(7, 'image', 'https://s3.amazonaws.com/novisignator/ads/aldo_bags.jpg', 'coupon_yes', true),
(11, 'image', 'https://s3.amazonaws.com/novisignator/ads/bug_tech.jpg', 'coupon_yes', true),
(12, 'image', 'https://s3.amazonaws.com/novisignator/ads/idigital_watch.jpg', 'coupon_yes', true),
(13, 'image', 'https://s3.amazonaws.com/novisignator/ads/bobby_perfume.jpg', 'coupon_yes', true),
(15, 'image', 'https://s3.amazonaws.com/novisignator/ads/pandora_bracelet.jpg', 'coupon_yes', true),
(21, 'image', 'https://s3.amazonaws.com/novisignator/ads/aroma_coffee.jpg', 'coupon_yes', true),
(23, 'image', 'https://s3.amazonaws.com/novisignator/ads/bk_meal.jpg', 'coupon_yes', true),
(24, 'image', 'https://s3.amazonaws.com/novisignator/ads/burgersbar_promo.jpg', 'coupon_yes', true);