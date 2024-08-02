from flask import jsonify, request
from functools import wraps
from jsonschema import validate, ValidationError


def validate_json(schema):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                validate(instance=request.json, schema=schema)
            except ValidationError as e:
                print(e)
                error_msg = f"Validation error in field: {e.path[0]} : {e.message}" if e.path else f"{e.message}"
                return make_response(400, "validation error", {}, f"Invalid data format: Error: {error_msg}")
            except Exception as e:
                print(e)
                return make_response(400, "exception", {}, "Invalid data format")
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def make_response(status, name_content, content=None, msg=""):
    body = {name_content: content}

    if msg:
        body["message"] = msg

    return jsonify(body), status
