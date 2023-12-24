from flask import jsonify


def make_response(data, status=200):
    return jsonify({
        "data": data,
        "status": 'OK' if status == 200 else 'Bad Request'
    })
