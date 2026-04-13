from flask import Blueprint,jsonify,request


def create_coupon_routes(coupon_service):
    coupon_bp = Blueprint('coupon', __name__)

    @coupon_bp.route('/coupon/<store_id>', methods=['GET'])
    def display_coupons(store_id):
        result = coupon_service.display_coupons(store_id)
        return jsonify(result)

    

    @coupon_bp.route('/coupon/claim', methods=['POST'])
    def claim_coupon():
        data = request.get_json()
        coupon_code = data['coupon_code']
        result = coupon_service.claim_coupon(coupon_code)
        return jsonify(result)
    
    return coupon_bp