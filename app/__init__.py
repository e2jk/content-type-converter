from flask import Flask

from config import Config

__version__ = "0.1.0"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    from app.main import bp as main_bp

    app.register_blueprint(main_bp)
    from app.xwwwformurlencoded2json import bp as xwwwformurlencoded2json_bp

    app.register_blueprint(
        xwwwformurlencoded2json_bp, url_prefix="/xwwwformurlencoded2json"
    )
    return app
