from . import smorest  #, migrate, sqlalchemy

def init_app(app, register_blueprints=None):
    smorest.init_app(app, register_blueprints)
    # sqlalchemy.init_app(app)
    # migrate.init_app(app, sqlalchemy.db)
