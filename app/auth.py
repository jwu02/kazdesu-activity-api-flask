from functools import wraps
from flask import request

from app.config import Config

def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return {"message": "Authorization header is missing"}, 401

        try:
            token_type, token = auth_header.split()
            if token_type != 'Bearer':
                return {"message": "Invalid token type"}, 401
            if token != Config.API_STATIC_TOKEN:
                return {"message": "Invalid token"}, 401
        except ValueError:
            return {"message": "Invalid authorization header format"}, 401
        
        return f(*args, **kwargs)

    return decorated_function