from datetime import datetime

from flask import request
from flask.views import MethodView
from sqlalchemy.sql.operators import desc_op

from api_v2.conexion import repo, repo_session
from api_v2.models import ModelContadores
from core.decorators import catch_errors
from core.responses import make_response




class ContadorService(MethodView):
    """
    Servicio para contador
    """
    decorators = [catch_errors]
    def get(self, id: int):
        with repo_session() as s:
            return make_response(s.query(ModelContadores).filter(ModelContadores.id == id).one_or_none())


class ContadoresService(MethodView):
    """
    Servicio para contadores
    """
    decorators = [catch_errors]

    def get(self):
        with repo_session() as s:
            contadores = s.query(ModelContadores).order_by(desc_op(ModelContadores.id)).all()
            return make_response([item.as_dict() for item in contadores])

    def post(self):

        model = ModelContadores()
        model.from_dict(request.get_json())
        model.fecha = datetime.date.isoformat()

        with repo_session() as s:
            s.add(model)
            s.commit()
            return make_response(model)
