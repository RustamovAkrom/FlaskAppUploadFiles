from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

def create_app(config_class = Config):
    app = Flask(__file__)
    app.config.from_object(config_class)
    
    from .routers import main_dp
    app.register_blueprint(main_dp)

    return app