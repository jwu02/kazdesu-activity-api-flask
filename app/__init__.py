from flask import Flask
from flask_restful import Api

from app.config import Config
from app.db import init_db
from app.resources import PingResource, KeyPressResource, LeftClickResource, RightClickResource, MouseMovementResource

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = Config.MONGO_URI

    init_db(app)

    api = Api(app)

    # Add resources to API
    api.add_resource(PingResource, '/api/v1/ping')
    api.add_resource(KeyPressResource, '/api/v1/key-presses')
    api.add_resource(LeftClickResource, '/api/v1/left-clicks')
    api.add_resource(RightClickResource, '/api/v1/right-clicks')
    api.add_resource(MouseMovementResource, '/api/v1/mouse-movements')

    return app
