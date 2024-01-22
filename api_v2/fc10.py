from flask import request
from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo_session
from api_v2.loggers import logger
from api_v2.models import ModelFC10
from core.decorators import catch_errors
from core.generators import last_report_id, current_date, set_report_id
from core.responses import make_response


class FC10Service(MethodView):
    decorators = [catch_errors]

    def post(self):
        data = request.get_json()
        logger.success(data)
        model = ModelFC10()
        model.from_dict(data)
        model.fecha = current_date()
        model.fecha_informe = current_date()
        model.numero = last_report_id("fc10")
        model.cont_informe = model.numero

        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                set_report_id("fc10", model.numero + 1)
                return make_response(model.as_dict())


class FC10ListService(MethodView):
    decorators = [catch_errors]

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC10).order_by(ModelFC10.id.desc()).all()
            logger.debug(lista)
        return make_response(lista)
