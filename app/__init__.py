from flask import Flask
from flask_restful import Api
import pymysql

from app.config import Config
from app.db import db
from app.resources import PingResource, KeyPressResource, LeftClickResource, RightClickResource, MouseMovementResource

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = Config.SQLALCHEMY_TRACK_MODIFICATIONS
    db.init_app(app)
    api = Api(app)

    # Ensure the database exists
    create_database_if_not_exists()

    # Create database tables
    with app.app_context():
        db.create_all()

    # Add resources to API
    api.add_resource(PingResource, '/api/v1/ping')  # Add ping resource
    api.add_resource(KeyPressResource, '/api/v1/key-presses')
    api.add_resource(LeftClickResource, '/api/v1/left-clicks')
    api.add_resource(RightClickResource, '/api/v1/right-clicks')
    api.add_resource(MouseMovementResource, '/api/v1/mouse-movements')

    return app


def create_database_if_not_exists():
    # Connect to MySQL server
    connection = pymysql.connect(
        host='localhost',
        user=Config.DB_USER,
        password=Config.DB_PASSWORD
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DB_NAME}")
            print(f"Database '{Config.DB_NAME}' is ready.")
    finally:
        connection.close()