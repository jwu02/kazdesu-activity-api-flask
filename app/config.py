import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    ACTIVITY_DB_NAME = os.getenv('ACTIVITY_DB_NAME')
    MONGO_URI = os.getenv('MONGO_URI')
    API_STATIC_TOKEN = os.getenv('API_STATIC_TOKEN')
