from flask import Blueprint,jsonify,request
from infrastructure.logger import get_logger
logger = get_logger(__name__)

def create_screen_routes(redis_client):

    screen_bp = Blueprint('screen',__name__)

    @screen_bp.route('/screen/current-ad',methods =['GET'])
    def current_ad():
        try:
            result = redis_client.get("screen:current_ad")
            if not result:
                return jsonify({"ad_url": None, "message": "No ad available"}), 404
            return jsonify({"ad_url": result})
        except Exception:
            logger.error("Redis unavailable in /screen/current-ad")
            return jsonify({"ad_url": None, "message": "Service unavailable"}), 503

        
    return screen_bp

