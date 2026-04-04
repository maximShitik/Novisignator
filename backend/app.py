from flask import Flask
from routes.chat import chat_bp
from routes.coupon import coupon_bp
from routes.navigation import navigation_bp
from routes.session import session_bp
from routes.admin import admin_bp

app = Flask(__name__)

app.register_blueprint(chat_bp)
app.register_blueprint(coupon_bp)
app.register_blueprint(navigation_bp)
app.register_blueprint(session_bp)
app.register_blueprint(admin_bp)

if __name__ == '__main__':
    app.run()