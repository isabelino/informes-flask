from functools import wraps

from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

from api_v2.loggers import logger


def catch_errors(f):
    """
    Decorador para captura de errores de SQLAlchemy y atributos
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            logger.debug(f"debug: " + str(args) + str(kwargs))
            return f(*args, **kwargs)
        except SQLAlchemyError as e:
            logger.error(repr(e))
            return jsonify({"data": str(e), "status": "Error"}), 400
        except AttributeError as e:
            logger.error(repr(e))
            return jsonify({"data": str(e), "status": "Error"}), 400
        except Exception as e:
            # Captura cualquier otra excepción no especificada anteriormente
            logger.error(repr(e))
            return jsonify({"data": str(e), "status": "Error"}), 400

    return decorated_function
