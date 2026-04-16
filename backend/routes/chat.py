from flask import Blueprint

chat_bp = Blueprint('chat', __name__)

def create_chat_route(chat_service):


    @chat_bp.route('/chat', methods=['POST'])
    def chat():
        pass

