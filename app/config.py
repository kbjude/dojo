import os


class BaseConfig(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_NAME = os.environ.get("DATABASE_NAME")
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
    DATABASE_USER = os.environ.get("DATABASE_USER")
    DATABASE_HOST = os.environ.get("DATABASE_HOST")
    DATABASE_PORT = os.environ.get("DATABASE_PORT")


# class Testing(BaseConfig):
#     TESTING = True
