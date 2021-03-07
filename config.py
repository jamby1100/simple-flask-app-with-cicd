import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgresql:///wordcount_dev"

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TESTING_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        # log to stderr
        Config.init_app(app)
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

class StagingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('STAGING_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        # log to stderr
        Config.init_app(app)
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

class ProductionConfig(Config):
    PROD = True
    SQLALCHEMY_DATABASE_URI = os.getenv('PRODUCTION_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        # log to stderr
        Config.init_app(app)
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

class PreProdConfig(Config):
    PROD = True
    SQLALCHEMY_DATABASE_URI = os.getenv('PREPROD_DATABASE_URI')

    @classmethod
    def init_app(cls, app):
        # log to stderr
        Config.init_app(app)
        import logging
        from logging import StreamHandler
        file_handler = StreamHandler()
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler)

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
    "preproduction": PreProdConfig
}