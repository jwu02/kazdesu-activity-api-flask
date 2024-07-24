from flask_restful import Resource
from flask import request

from app.db import db
from app.auth import token_required
from app.models import LeftClick

class LeftClickResource(Resource):
    @token_required
    def post(self):
        data = request.json
        count = data.get('count')
        created_at = data.get('createdAt')

        try:
            left_click = LeftClick(count=count, created_at=created_at)
            db.session.add(left_click)
            db.session.commit()
            return {"message": "Left click data inserted successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"message": f"Error inserting data: {str(e)}"}, 500

    def get(self):
        left_clicks = LeftClick.query.all()
        result = [
            {
                'id': lc.id,
                'count': lc.count, 
                'createdAt': lc.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
            } for lc in left_clicks
        ]
        return {'data': result}, 200