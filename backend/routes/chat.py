from flask import Blueprint,jsonify,request


def create_chat_routes(chat_service):
    chat_bp = Blueprint('chat', __name__)

    @chat_bp.route('/chat', methods=['POST'])
    def chat():
        session_id = request.cookies.get('session_id')
        data = request.get_json()
        input = data['message']
        result = chat_service.handle_message(session_id,input)
        return jsonify(result)
    return chat_bp
