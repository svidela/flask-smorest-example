from flask_smorest import Api

api = Api()

def init_app(app, register_blueprints=None):
    api.init_app(app)
    register_blueprints(api)
