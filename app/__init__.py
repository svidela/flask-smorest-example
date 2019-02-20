from flask import Flask

from flask_rest_api import Api
from apispec.ext.marshmallow import MarshmallowPlugin

from config import config

# Flask extensions-related objetcs
# db = SQLAlchemy()
# migrate = Migrate()
api = Api()

from . import models


def create_app(cfg='default'):
    app = Flask(__name__)

    app.config.from_object(config[cfg])
    config[cfg].init_app(app)

    # Initialize Flask extensions-related objects
    # db.init_app(app)
    # migrate.init_app(app, db)


    # Make sure to import all your schemas in /app/resources/__init__.py
    from . import resources

    # Setting schema_name_resolver to the constant function False avoids
    # having apispec registering nested schemas automatically.
    # We use flask-rest-api api decorator for that.
    ma_plugin = MarshmallowPlugin(schema_name_resolver=lambda _: False)
    api.init_app(app, spec_kwargs=dict(marshmallow_plugin=ma_plugin))
    resources.register_blueprints(api)

    return app
