from functools import wraps

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError


def catch_errors(f):
    """
    Decorador para captura de errores de SQLAlchemy
    :param f:
    :return:
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except SQLAlchemyError as e:
            return jsonify({"data": repr(e), "status": "Error"}), 400
    return decorated_function
