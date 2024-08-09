from flask_restful import Resource
from flask import request

from app.db import get_db
from app.auth import token_required

class MouseMovementResource(Resource):
    @token_required
    def post(self):
        data = request.json
        amount = data.get('amount')
        created_at = data.get('createdAt')

        try:
            db = get_db()
            db.mouse_movements.insert_one({
                'amount': amount,
                'createdAt': created_at
            })
            return {"message": "Mouse movement data inserted successfully"}, 201
        except Exception as e:
            return {"message": f"Error inserting data: {str(e)}"}, 500

    def get_data(self):
        try:
            db = get_db()
            mouse_movements = db.mouse_movements.find()
            result = [
                {
                    'id': str(mm['_id']),
                    'amount': mm['amount'], 
                    'createdAt': mm['createdAt']
                } for mm in mouse_movements]
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