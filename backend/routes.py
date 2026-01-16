from flask import Blueprint, jsonify

from db import fetch_all
from queries import GET_STORES

api_bp = Blueprint("api", __name__)


@api_bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@api_bp.route("/stores", methods=["GET"])
def get_stores():
    stores = fetch_all(GET_STORES)
    return jsonify({"stores": stores})