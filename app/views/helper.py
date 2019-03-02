import datetime
import jwt
from functools import wraps
from flask import request, jsonify
from app.models.user_model import User


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        if 'auth_token' in request.headers:
            token = request.headers['auth_token']

        if not token:
            return jsonify({
                "status": 400,
                "message": "Token  missing"
            }), 400
        try:
            user_id = User.decode_auth_token(token)
            current_user = user_id
            if not isinstance(current_user, int):
                return jsonify({
                    "message":current_user
                })

        except:
            message = "Invalid token"
            decode_response = User.decode_auth_token(token)
            if isinstance(decode_response, str):
                message = decode_response
            return jsonify({
                "status": "failed",
                "message": message
            }), 401

        return func(current_user, *args, **kwargs)

    return decorated
