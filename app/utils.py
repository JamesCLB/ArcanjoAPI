from flask import jsonify, request
from functools import wraps
from jsonschema import validate, ValidationError


def validate_json(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            validate(instance=request.json, schema=schema)
            return f(*args, **kwargs)

        return decorated_function

    return decorator


def make_response(status, name_content, content=None, msg=""):
    body = {name_content: content}

    if msg:
        body["message"] = msg

    return jsonify(body), status
