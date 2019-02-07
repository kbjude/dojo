import os

class Config:
  DEBUG = False
  TESTING = False
  SECRET_KEY = ("SECRET_KEY", "thisismysercetkey")

# class DevelopmentConfig(Config):
#   DEBUG = True

# class TestingConfig(Config):
#   DEBUG = True
#   TESTING = True

# class ProductionConfig(Config):
#   DEBUG = False