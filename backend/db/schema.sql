

CREATE TABLE IF NOT EXISTS stores (
  store_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  store_name    TEXT NOT NULL UNIQUE,
  category      TEXT NOT NULL,
  floor         INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS scan_points(
  scan_point_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  scan_point_name    TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS store_navigation (
  store_id      INTEGER NOT NULL,
  scan_point_id INTEGER NOT NULL,
  route_path_d  TEXT NOT NULL,

  PRIMARY KEY (store_id, scan_point_id),
  FOREIGN KEY (store_id) REFERENCES stores(store_id) ON DELETE CASCADE,
  FOREIGN KEY (scan_point_id) REFERENCES scan_points(scan_point_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS products (
  product_id     INTEGER GENERATED ALWAYS AS IDENTITY,
  product_name   TEXT NOT NULL,
  category       TEXT NOT NULL,
  PRIMARY KEY (product_id)
);

CREATE TABLE IF NOT EXISTS store_products(
  product_id  INTEGER NOT NULL,
  store_id    INTEGER NOT NULL,
  PRIMARY KEY (store_id, product_id),
  FOREIGN KEY (store_id) REFERENCES stores(store_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS coupons (
  store_id     INTEGER NOT NULL,
  coupon_code  TEXT NOT NULL,
  description   TEXT NOT NULL ,

  PRIMARY KEY (coupon_code),
  FOREIGN KEY (store_id) REFERENCES stores(store_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS ads (
  ad_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  store_id   INTEGER NOT NULL,
  ad_type    TEXT    NOT NULL CHECK (ad_type IN ('image', 'navigation')),
  asset_url  TEXT    NOT NULL,
  trig       TEXT    NOT NULL CHECK (trig IN ('default', 'coupon_yes')),
  is_active  BOOLEAN NOT NULL DEFAULT TRUE,
  created_at TIMESTAMP NOT NULL DEFAULT NOW(),

  FOREIGN KEY (store_id) REFERENCES stores(store_id) ON DELETE CASCADE
);


CREATE INDEX IF NOT EXISTS idx_products_name ON products(product_name);
CREATE INDEX IF NOT EXISTS idx_products_category ON products(category);
CREATE INDEX IF NOT EXISTS idx_ads_store_trigger_active ON ads (store_id, trig, is_active);
CREATE INDEX IF NOT EXISTS idx_ads_store_type_active ON ads (store_id, ad_type, is_active);