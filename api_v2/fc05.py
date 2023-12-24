from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelFC05
from core.decorators import catch_errors
from core.responses import make_response


class FC05Service(MethodView):
    decorators = [catch_errors]

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC05).all()
            return make_response([item.as_dict() for item in lista])


class FC05ItemsService(MethodView):
    decorators = [catch_errors]

    def get(self, month: int, year: int):
        # todo add month and year logic; see def fc05_items(m, y)
        with repo_session() as s:
            return make_response(s.query(ModelFC05).all())


class FC05ByDateService(MethodView):
    decorators = [catch_errors]

    def get(self, date):
        with repo_session() as s:
            lista = s.query(ModelFC05).filter(ModelFC05.fecha == date).all()
            return make_response([item.as_dict() for item in lista])
