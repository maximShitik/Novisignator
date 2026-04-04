from flask import Blueprint


session_bp = Blueprint('session',__name__)

@session_bp.route('/session/start', methods=['POST'])
def start_session():
    pass
