from flask import request
from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo_session
from api_v2.models import ModelFC05
from core.decorators import catch_errors
from core.generators import last_report_id, set_report_id
from core.responses import make_response


class FC05Service(MethodView):
    decorators = [catch_errors]

    # def get(self):
    #     with repo_session() as s:
    #         lista = s.query(ModelFC05).all()
    #         return make_response([item.as_dict() for item in lista])

    def post(self):
        from api_v2.loggers import logger
        data = request.get_json()
        logger.warning(data)
        model = ModelFC05()
        model.from_dict(data)
        logger.success(model.as_dict())
        # model.fecha = current_date()
        model.numero = last_report_id("fc05")

        set_report_id("fc05", model.numero + 1)

        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                logger.error(repr(e))
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                logger.success(model.as_dict())
                return make_response(model.as_dict())


class FC05ListService(MethodView):
    decorators = [catch_errors]

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC05).order_by(ModelFC05.id.desc()).all()
        return make_response(lista)


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
