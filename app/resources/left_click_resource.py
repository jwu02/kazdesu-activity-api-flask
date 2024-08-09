from flask_restful import Resource
from flask import request

from app.db import get_db
from app.auth import token_required

class LeftClickResource(Resource):
    @token_required
    def post(self):
        data = request.json
        count = data.get('count')
        created_at = data.get('createdAt')

        try:
            db = get_db()
            db.left_clicks.insert_one({
                'count': count,
                'createdAt': created_at
            })
            return {"message": "Left click data inserted successfully"}, 201
        except Exception as e:
            return {"message": f"Error inserting data: {str(e)}"}, 500

    def get_data(self):
        try:
            db = get_db()
            left_clicks = db.left_clicks.find()
            result = [
                {
                    'id': str(lc['_id']),
                    'count': lc['count'], 
                    'createdAt': lc['createdAt']
                } for lc in left_clicks
            ]
            return result
        except Exception as e:
            return {"message": f"Error retrieving data: {str(e)}"}
    
    def get(self):
        statusCode = 200
        try:
            result = self.get_data()
        except Exception as e:
            statusCode = 500
        finally:
            return result, statusCode