from flask_restful import Resource

class PingResource(Resource):
    def get(self):
        return {"status": "up"}, 200