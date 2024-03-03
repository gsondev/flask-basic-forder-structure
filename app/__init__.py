import os
import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app():
    app = Flask(__name__)
    env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
    app.config.from_object(env_config)
    db.init_app(app)
    with app.app_context():
        
        from .routes import base_api
        app.register_blueprint(base_api)
        
        return app