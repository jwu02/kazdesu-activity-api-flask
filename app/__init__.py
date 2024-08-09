from flask import Flask, render_template, redirect, url_for
from flask_restful import Api

from app.config import Config
from app.db import init_db
from app.resources import PingResource, KeyPressResource, LeftClickResource, RightClickResource, MouseMovementResource, AllActivityResource

route_to_resource_mapping = {
    '/api/v1/ping': PingResource,
    '/api/v1/activity/key-presses': KeyPressResource,
    '/api/v1/activity/left-clicks': LeftClickResource,
    '/api/v1/activity/right-clicks': RightClickResource,
    '/api/v1/activity/mouse-movements': MouseMovementResource,
    '/api/v1/activity/all': AllActivityResource
}

def create_app():
    app = Flask(__name__)
    app.config['MONGO_URI'] = Config.MONGO_URI

    init_db(app)

    api = Api(app)

    @app.route('/')
    def index():
        return render_template('index.html', valid_endpoints=list(route_to_resource_mapping.keys()))
    
    # Error handler for 404
    @app.errorhandler(404)
    def page_not_found(e):
        """
        Redirect all invalid route requests to index page
        """
        return redirect(url_for('index'))

    # Add resources to API
    for route, resource in route_to_resource_mapping.items():
        api.add_resource(resource, route)

    return app
