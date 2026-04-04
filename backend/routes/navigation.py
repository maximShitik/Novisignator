from flask import Blueprint

navigation_bp = Blueprint('navigation', __name__)


@navigation_bp.route('/navigate', methods=['GET'])
def get_svg():
    pass
