from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelFC03
from core.responses import make_response


class FC03Service(MethodView):

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC03).all()
            return make_response([item.as_dict() for item in lista])


class FC03ByDateService(MethodView):
    def get(self, date):
        with repo_session() as s:
            list = s.query(ModelFC03).filter(ModelFC03.fecha == date).all()
            return make_response([item.as_dict() for item in list])
