from flask import Blueprint

coupon_bp = Blueprint('coupon', __name__)

@coupon_bp.route('/coupon/claim', methods=['POST'])
def claim_coupon():
    pass

@coupon_bp.route('/coupon', methods=['GET'])
def get_coupon():
    pass
