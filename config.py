import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    ACCESS_KEY_ID = os.environ.get("ACCESS_KEY_ID")
    SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")
    SESSION_TOKEN = os.environ.get("SESSION_TOKEN")
    REGION = os.environ.get("REGION")

    LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """Class DevelopmentConfig.

    This class defines the development configuration for the application.

    Attributes:
        FLASK_CONFIG (str): The Flask configuration set to "DEV".
        TESTING (bool): Flag indicating if the application is running in testing mode.
        DEBUG (bool): Flag indicating if the application is running in debug mode.

    """
    FLASK_CONFIG = "DEV"
    TESTING = True
    DEBUG = True


class TestingConfig(Config):
    """
    A class used to define the testing configuration for a Flask application.

    Inherits from Config class.

    Attributes:
        FLASK_CONFIG (str): The flask configuration set to "TEST".
        TESTING (bool): Flag to indicate if the application is running in testing mode.
        DEBUG (bool): Flag to indicate if debug mode is enabled for the application.

    """
    FLASK_CONFIG = "TEST"
    TESTING = True
    DEBUG = True


class StagingConfig(Config):
    """

    class StagingConfig(Config):
        FLASK_CONFIG = "STAGING"
        TESTING = False
        DEBUG = False

    """
    FLASK_CONFIG = "STAGING"
    TESTING = False
    DEBUG = False


class ProductionConfig(Config):
    """
    A class representing the configuration for a production environment.

    This class is a subclass of the Config class. It defines the configuration settings specifically for a production environment.

    Attributes:
        FLASK_CONFIG (str): A string representing the Flask configuration. Set to "PROD" for production.
        TESTING (bool): A boolean indicating whether testing mode is enabled. Set to False for production.
        DEBUG (bool): A boolean indicating whether debug mode is enabled. Set to False for production.
    """
    FLASK_CONFIG = "PROD"
    TESTING = False
    DEBUG = False


config = {
    "DEV": DevelopmentConfig,
    "TEST": TestingConfig,
    "STAGING": StagingConfig,
    "PROD": ProductionConfig,
    "default": DevelopmentConfig,
}
