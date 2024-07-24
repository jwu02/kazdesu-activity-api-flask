from flask_restful import Resource
from flask import request

from app.db import db
from app.auth import token_required
from app.models import RightClick

class RightClickResource(Resource):
    @token_required
    def post(self):
        data = request.json
        count = data.get('count')
        created_at = data.get('createdAt')

        try:
            right_click = RightClick(count=count, created_at=created_at)
            db.session.add(right_click)
            db.session.commit()
            return {"message": "Right click data inserted successfully"}, 201
        except Exception as e:
            db.session.rollback()
            return {"data": f"Error inserting data: {str(e)}"}, 500

    def get(self):
        right_clicks = RightClick.query.all()
        result = [
            {
                'id': rc.id,
                'count': rc.count, 
                'createdAt': rc.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
            } for rc in right_clicks]
        return {'data': result}, 200