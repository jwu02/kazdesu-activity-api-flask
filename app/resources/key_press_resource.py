from flask_restful import Resource
from flask import request

from app.db import db
from app.auth import token_required
from app.models import KeyPress

class KeyPressResource(Resource):
    @token_required
    def post(self):
        data = request.json
        count = data.get('count')
        created_at = data.get('createdAt')
        print(created_at)

        try:
            key_press = KeyPress(count=count, created_at=created_at)
            db.session.add(key_press)
            db.session.commit()
            return {"message": "Key press data inserted successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"Error inserting data: {str(e)}"}, 500

    def get(self):
        key_presses = KeyPress.query.all()
        result = [
            {
                'id': kp.id,
                'count': kp.count, 
                'createdAt': kp.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
            } for kp in key_presses
        ]
        return {'data': result}, 200