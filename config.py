import os

class Config:
    '''
    This is the general configuration parent class
    '''

    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    '''
    This is the production configuration child class
    '''
    pass


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://MacbookAir:sam123@localhost/blog'


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}