from flask import Flask
from routes.chat import chat_bp
from routes.coupon import create_coupon_routes
from routes.navigation import navigation_bp
from routes.session import session_bp
from routes.admin import admin_bp

from infrastructure.kafka import create_kafka_producer
from infrastructure.db import create_db_pool
from repositories.coupon_repository import CouponRepository
from services.coupon_service import CouponService

DATABASE_URL = "postgresql://user:password@localhost/malldb"
KAFKA_SERVERS = "localhost:9092"

kafka_producer = create_kafka_producer(KAFKA_SERVERS)
db_pool = create_db_pool(DATABASE_URL)


coupon_repo = CouponRepository(db_pool)
coupon_service = CouponService(coupon_repo, kafka_producer)
coupon_bp = create_coupon_routes(coupon_service)

app = Flask(__name__)

app.register_blueprint(chat_bp)
app.register_blueprint(coupon_bp)
app.register_blueprint(navigation_bp)
app.register_blueprint(session_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run()