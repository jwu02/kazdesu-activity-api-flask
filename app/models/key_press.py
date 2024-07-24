from app.db import db

class KeyPress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)
    # https://stackoverflow.com/questions/13370317/sqlalchemy-default-datetime
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)