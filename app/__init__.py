from flask import Flask

from flask_rest_api import Api
from config import config

# Flask extensions-related objetcs
# db = SQLAlchemy()
# migrate = Migrate()
from . import models, resources


def create_app(cfg='default'):
    app = Flask(__name__)

    app.config.from_object(config[cfg])
    config[cfg].init_app(app)

    # Initialize Flask extensions-related objects
    # db.init_app(app)
    # migrate.init_app(app, db)

    api = Api()
    api.init_app(app)

    resources.register_blueprints(api)

    return app
