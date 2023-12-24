from flask.views import MethodView

from api_v2.conexion import repo
from core.decorators import catch_errors
from core.responses import make_response


class Prueba(MethodView):
    """
    Servicio para prueba
    """
    decorators = {catch_errors}
    def get(self):
        with repo() as db:
            _timestamp = db.fetch_scalar('SELECT CURRENT_TIMESTAMP')
            return make_response(_timestamp)
