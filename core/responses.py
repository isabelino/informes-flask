from flask import jsonify, Response


def make_response(data, status=200):
    """
    Crear una respuesta personalizada
    :param data:
    :param status:
    :return:
    """

    def response_code_str(code=200)->str:

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



    return jsonify({
        "data": data,
        "status": response_code_str(status)
    }), status
