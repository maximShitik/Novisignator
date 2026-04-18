from flask import Flask, jsonify

# ── Mock Infrastructure ──────────────────────────────────────────────

class MockRedis:
    def __init__(self):
        self.store = {}
    def get(self, key):
        return self.store.get(key)
    def set(self, key, value, ex=None):
        self.store[key] = value

class MockKafka:
    def publish(self, topic, message):
        print(f"[MOCK KAFKA] topic={topic} message={message}")

class MockS3:
    def generate_presigned_url(self, key):
        return f"https://mock-s3.com/{key}"

class MockLLM:
    def parse(self, message):
        return { "intent": "find_store", "params": { "store_name": "Nike" } }

# ── Mock Repositories ────────────────────────────────────────────────

class MockCouponRepo:
    def get_by_code(self, coupon_code):
        if coupon_code == "NIKE10":
            return (3, "NIKE10", "10% off all shoes")
        return None
    def get_by_store(self, store_id):
        return [
            (3, "NIKE10", "10% off all shoes"),
            (3, "NIKE20", "20% off jackets"),
        ]

class MockStoreRepo:
    def get_by_name(self, store_name):
        return [(3, "Nike", "Shoes", 2)]

class MockProductRepo:
    def get_by_name(self, product_name):
        return [(1, "Air Max", "Shoes")]

class MockNavigationRepo:
    def get_navigation_route(self, scan_point_id, store_id):
        return (3, 1, "M 100 200 L 300 400")
    def get_all_routes(self):
        return [
            (1, 1, "M 100 200 L 300 400"),
            (1, 2, "M 150 250 L 350 450"),
        ]

# ── Wire Everything ──────────────────────────────────────────────────

from services.coupon_service import CouponService
from services.chat_service import ChatService
from services.navigation_service import NavigationService

from routes.coupon import create_coupon_routes
from routes.chat import create_chat_routes
from routes.navigation import create_navigation_route
from routes.session import create_session_route
from routes.screen import create_screen_routes

redis_client = MockRedis()
kafka_client = MockKafka()
s3_client = MockS3()
llm_client = MockLLM()

coupon_repo = MockCouponRepo()
store_repo = MockStoreRepo()
product_repo = MockProductRepo()
navigation_repo = MockNavigationRepo()

coupon_service = CouponService(coupon_repo, kafka_client)
navigation_service = NavigationService(navigation_repo, redis_client)
chat_service = ChatService(store_repo, product_repo, redis_client, llm_client, navigation_service)

coupon_bp = create_coupon_routes(coupon_service)
chat_bp = create_chat_routes(chat_service)
navigation_bp = create_navigation_route(navigation_service)
session_bp = create_session_route(redis_client)
screen_bp = create_screen_routes(redis_client)

app = Flask(__name__)

app.register_blueprint(coupon_bp)
app.register_blueprint(chat_bp)
app.register_blueprint(navigation_bp)
app.register_blueprint(session_bp)
app.register_blueprint(screen_bp)

navigation_service.warm_cache()

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)