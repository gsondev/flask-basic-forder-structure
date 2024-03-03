import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

if os.path.exists(dotenv_path):
  load_dotenv(dotenv_path)
  
class Config:
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  JWT_KEY = os.getenv('JWT_KEY')
  DB_HOST = os.getenv('DB_HOST')
  DB_NAME = os.getenv('DB_NAME')
  DB_PORT = os.getenv('DB_PORT')
  DB_PASS = os.getenv('DB_PASS')
  DB_USER = os.getenv('DB_USER')
  SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
  
class DevelopmentConfig(Config):
  DEBUG = True
  ENV = 'development'

class ProductionConfig(Config):
  DEBUG = False
  ENV = 'production'