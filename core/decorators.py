from functools import wraps
from http.client import HTTPResponse

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
            return jsonify({"data": str(e), "status": "Error"}), HTTPResponse.BAD_REQUEST
    return decorated_function
