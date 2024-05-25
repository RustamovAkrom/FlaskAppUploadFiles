from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

app = Flask(__file__)
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class = Config):
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app)

    from .routers import main_dp
    app.register_blueprint(main_dp)

    return app