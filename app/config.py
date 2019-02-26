import os

class BaseConfig:
  DEBUG = False
  TESTING = False
  SECRET_KEY = os.environ.get("SECRET_KEY", "thisismysercetkey")
  DATABASE_NAME = os.environ.get("DATABASE_NAME", "jenny")
  DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD", "postgres")
  DATABASE_USER = os.environ.get("DATABASE_USER", "postgres")
  DATABASE_HOST = os.environ.get("DATABASE_HOST", "localhost")
  DATABASE_PORT = os.environ.get("DATABASE_PORT", "5432")

class Development(BaseConfig):
  DEBUG = True

# class Testing(Config):
  # DEBUG = True
  # TESTING = True

class Production(BaseConfig):
  DEBUG = False

configuration = {
  "development":Development,
  "production": Production
  }