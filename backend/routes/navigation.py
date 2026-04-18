from flask import Blueprint, jsonify



def create_navigation_route(navigation_service):

    navigation_bp = Blueprint('navigation', __name__)

    @navigation_bp.route('/navigate/<scan_point_id>/<store_id>', methods=['GET'])
    def get_svg(scan_point_id, store_id):
        result = navigation_service.get_route(scan_point_id, store_id)
        return jsonify({"route": result})
    return navigation_bp