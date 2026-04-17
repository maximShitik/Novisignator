from flask import Flask,jsonify
from routes.chat import create_chat_routes
from routes.coupon import create_coupon_routes
from routes.navigation import create_navigation_route
from routes.session import create_session_route
from routes.screen import create_screen_routes 

from routes.admin import admin_bp

from infrastructure.kafka import MallKafkaProducer
from infrastructure.db import create_db_pool
from infrastructure.redis import create_redis_client
from infrastructure.s3 import MallS3
from infrastructure.llm import LLM

from services.chat_service import ChatService
from services.coupon_service import CouponService
from services.navigation_service import NavigationService

from repositories.coupon_repository import CouponRepository
from repositories.store_repository import StoreRepository
from repositories.product_repository import ProductRepository
from repositories.navigation_repository import NavigationRepository

from backend.consts import DATABASE_URL,KAFKA_SERVERS,REDIS_HOST,REDIS_PORT,AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,S3_BUCKET,OPENAI_API_KEY,MODEL
from infrastructure.logger import get_logger
logger = get_logger(__name__)

 
kafka_producer = MallKafkaProducer(KAFKA_SERVERS)
db_pool = create_db_pool(DATABASE_URL)
redis_client = create_redis_client(REDIS_HOST,REDIS_PORT)
llm_client = LLM(OPENAI_API_KEY, MODEL)
s3_client = MallS3(AWS_ACCESS_KEY, AWS_SECRET_KEY, AWS_REGION, S3_BUCKET)

coupon_repo = CouponRepository(db_pool)
store_repo = StoreRepository(db_pool)
product_repo = ProductRepository(db_pool)
navigation_repo = NavigationRepository(db_pool)

coupon_service = CouponService(coupon_repo, kafka_producer)
navigation_service = NavigationService(navigation_repo,redis_client)
chat_service = ChatService(store_repo,product_repo,redis_client,llm_client,navigation_service)


coupon_bp = create_coupon_routes(coupon_service)
chat_bp = create_chat_routes(chat_service)
navigation_bp = create_navigation_route(navigation_service)
session_bp = create_session_route(redis_client)
screen_bp = create_screen_routes(redis_client)

app = Flask(__name__)

app.register_blueprint(chat_bp)
app.register_blueprint(coupon_bp)
app.register_blueprint(navigation_bp)
app.register_blueprint(session_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(screen_bp)
navigation_service.warm_cache()


@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {e}")
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run()