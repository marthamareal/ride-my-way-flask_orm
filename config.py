import os

from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

class BaseConfig(object):

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', default='postgresql://localhost/learn_app')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI', default='postgresql://localhost/learn_app_test')
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
