from typing import Optional

from flask import jsonify


def make_response(data: Optional[str | Exception], status=200):
    """
    Crear una respuesta personalizada
    :param data:
    :param status:
    :return:
    """

    def response_code_str(code=200) -> str:
        # all http status
        code_table = {
            200: 'OK',
            201: 'Created',
            400: 'Bad Request',
            404: 'Not Found',
            405: 'Method Not Allowed',
            500: 'Internal Server Error'
        }

        return code_table[code] or 'Bad Request'

    if isinstance(data, Exception):
        status = 400
        data = repr(data)

    return jsonify({
        "data": data,
        "status": response_code_str(status)
    }), status
