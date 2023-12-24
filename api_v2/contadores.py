from flask.views import MethodView

from api_v2.conexion import repo, repo_session
from api_v2.models import ModelContadores


class ContadoresService(MethodView):

    def get(self):
        with repo_session() as s:
            contadores = s.query(ModelContadores).all()
            return contadores
