from flask import Blueprint,jsonify,request


def create_chat_routes(chat_service):
    chat_bp = Blueprint('chat', __name__)

    @chat_bp.route('/chat', methods=['POST'])
    def chat():
        data = request.get_json()
        input = data['message']
        result = chat_service.handle_message(input)
        return jsonify(result)
    return chat_bp
