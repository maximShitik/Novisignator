from flask import Blueprint,jsonify,request
import uuid

def create_session_route(redis_client):
    session_bp = Blueprint('session',__name__)

    @session_bp.route('/session/create',methods =['GET'])
    def create():
        session_id = str(uuid.uuid4())
        response = jsonify({"success": True})
        response.set_cookie('session_id', session_id, httponly=True)
        redis_client.set(f"session:{session_id}", "active")
        return response


    @session_bp.route('/session/scan', methods=['POST'])
    def scan():
        session_id = request.cookies.get('session_id')
        data = request.get_json()
        scan_point_id = data['scan_point_id']
        redis_client.set(f"session:{session_id}:scan_point", scan_point_id)
        return jsonify({"scan_point_id": scan_point_id})

    return session_bp