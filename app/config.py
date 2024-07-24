import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    API_STATIC_TOKEN = os.getenv('API_STATIC_TOKEN')
