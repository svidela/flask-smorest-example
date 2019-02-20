# import os


class Config:
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    # This is required even if we don't want to serve the spec
    OPENAPI_VERSION = '3.0.2'
    OPENAPI_URL_PREFIX = 'openapi'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL')

    OPENAPI_REDOC_PATH = 'redoc'
    OPENAPI_REDOC_VERSION = 'next'
    OPENAPI_SWAGGER_UI_PATH = 'swagger-ui'
    OPENAPI_SWAGGER_UI_VERSION = '3.18.3'


class TestingConfig(Config):
    TESTING = True

    # SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL')


class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = os.getenv('PROD_DATABASE_URL')
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
