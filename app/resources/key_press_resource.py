from flask_restful import Resource
from flask import request

from app.db import get_db
from app.auth import token_required

class KeyPressResource(Resource):
    @token_required
    def post(self):
        data = request.json
        count = data.get('count')
        created_at = data.get('createdAt')

        if not isinstance(count, int):
            return {"message": "Invalid count value. It must be an integer."}, 400
        
        try:
            # Insert data into MongoDB
            db = get_db()
            db.key_presses.insert_one({
                'count': count,
                'createdAt': created_at
            })
            return {"message": "Key press data inserted successfully"}, 201
        except Exception as e:
            return {"message": f"Error inserting data: {str(e)}"}, 500

    def get(self):
        try:
            db = get_db()
            key_presses = db.key_presses.find()
            result = [
                {
                    'id': str(kp['_id']),
                    'count': kp['count'],
                    'createdAt': kp['createdAt']
                } for kp in key_presses
            ]
            return {'data': result}, 200
        except Exception as e:
            return {"message": f"Error retrieving data: {str(e)}"}, 500