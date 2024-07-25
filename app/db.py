from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def init_db(app):
    mongo.init_app(app)

def get_db():
    return mongo.cx[Config.ACTIVITY_DB_NAME]