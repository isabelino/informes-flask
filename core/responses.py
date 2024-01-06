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
            202: 'Accepted',
            203: 'Non-Authoritative Information',
            204: 'No Content',
            205: 'Reset Content',
            206: 'Partial Content',

            300: 'Multiple Choices',
            301: 'Moved Permanently',
            302: 'Found',
            303: 'See Other',
            304: 'Not Modified',
            305: 'Use Proxy',
            306: 'Switch Proxy',
            307: 'Temporary Redirect',
            308: 'Permanent Redirect',

            400: 'Bad Request',
            401: 'Unauthorized',
            402: 'Payment Required',
            403: 'Forbidden',
            404: 'Not Found',
            405: 'Method Not Allowed',
            406: 'Not Acceptable',
            407: 'Proxy Authentication Required',
            408: 'Request Timeout',
            409: 'Conflict',
            410: 'Gone',
            411: 'Length Required',
            412: 'Precondition Failed',
            413: 'Request Entity Too Large',
            414: 'Request URI Too Long',
            415: 'Unsupported Media Type',
            416: 'Requested Range Not Satisfiable',
            417: 'Expectation Failed',
            418: 'I\'m a teapot',
            421: 'Misdirected Request',
            422: 'Unprocessable Entity',
            423: 'Locked',
            424: 'Failed Dependency',
            426: 'Upgrade Required',
            428: 'Precondition Required',
            429: 'Too Many Requests',
            431: 'Request Header Fields Too Large',

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
