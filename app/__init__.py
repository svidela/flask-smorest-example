from flask import Flask

from config import config

from . import extensions, resources


def create_app(cfg='default'):
    app = Flask(__name__)

    app.config.from_object(config[cfg])
    config[cfg].init_app(app)

    extensions.init_app(app, register_blueprints=resources.register_blueprints)

    return app
