from functools import wraps
from flask import request, g, jsonify
from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import SignatureExpired, BadSignature
from app import app

TWO_WEEKS = 1209600

SECRET_KEY = app.config["SECRET_KEY"]

def generate_token(user):
    s = Serializer(SECRET_KEY)

    token = s.dumps({
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name
    })

    return token


def verify_token(token):
    s = Serializer(SECRET_KEY)

    try:
        data = s.loads(token, max_age=TWO_WEEKS)
        return data

    except SignatureExpired:
        return None

    except BadSignature:
        return None

def requires_auth(f):


 @wraps(f)
 def decorated(*args, **kwargs):

    token = request.headers.get("Authorization", None)

    if token:
        user = verify_token(token)

        if user:
            g.current_user = user
            return f(*args, **kwargs)

    return jsonify(
        message="Authentication is required to access this resource"
    ), 401

 return decorated

