from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelFC06


class FC06Service(MethodView):

    def get(self):
        pass


class FC06ItemsService(MethodView):

    def get(self, year: int):
        with repo_session() as s:
            lista = s.query(ModelFC06) \
                .aggregate(ModelFC06.year) \
                .filter(ModelFC06.year == year) \
                .group_by(ModelFC06.year) \
                .all()
            return make_response([item.as_dict() for item in lista])
