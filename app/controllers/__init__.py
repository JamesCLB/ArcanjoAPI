from flask import jsonify


def make_response(status, name_content, content=None, msg=""):
    body = {name_content: content}

    if msg:
        body = {"message": msg}

    return jsonify(body), status
