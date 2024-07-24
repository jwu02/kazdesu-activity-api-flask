from flask_restful import Resource
from flask import request

from app.db import db
from app.auth import token_required
from app.models import MouseMovement

class MouseMovementResource(Resource):
    @token_required
    def post(self):
        data = request.json
        amount = data.get('amount')
        created_at = data.get('createdAt')

        try:
            mouse_movement = MouseMovement(amount=amount, created_at=created_at)
            db.session.add(mouse_movement)
            db.session.commit()
            return {"message": "Mouse movement data inserted successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"Error inserting data: {str(e)}"}, 500

    def get(self):
        mouse_movements = MouseMovement.query.all()
        result = [
            {
                'id': mm.id,
                'amount': mm.amount, 
                'createdAt': mm.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
            } for mm in mouse_movements]
        return {'data': result}, 200