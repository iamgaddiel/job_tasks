from flask import Flask

from config import Config
from extensions import flask_jwt_ext


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Extensions
    flask_jwt_ext.init_app(app)

    # App blueprints
    from .template import template_bp
    from .auth import auth_bp


    # Blueprint registrations
    app.register_blueprint(template_bp)
    app.register_blueprint(auth_bp)

    return app