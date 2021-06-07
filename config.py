# import os


class Config:
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    API_TITLE = "App Name"
    API_VERSION = "v1"
    OPENAPI_VERSION = "3.0.3"
    OPENAPI_URL_PREFIX = "openapi"

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')

    OPENAPI_REDOC_PATH = "/redoc"
    OPENAPI_REDOC_URL = "https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"

    OPENAPI_SWAGGER_UI_PATH = "/swagger-ui"
    OPENAPI_SWAGGER_UI_URL = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    OPENAPI_RAPIDOC_PATH = "rapidoc"
    OPENAPI_RAPIDOC_URL = "https://cdn.jsdelivr.net/npm/rapidoc/dist/rapidoc-min.js"
    
    SOME_CONFIG = 'xyz'


class TestingConfig(Config):
    TESTING = True
    SOME_CONFIG = 'foo'
    # SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
    SOME_CONFIG = 'bar'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
