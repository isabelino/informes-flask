import datetime

from flask import request
from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo, repo_session
from api_v2.models import ModelFC06
from api_v2.scripts import Informe06ItemsScript
from core.decorators import catch_errors
from core.generators import last_report_id
from core.responses import make_response


class FC06Service(MethodView):
    decorators = [catch_errors]

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        model = ModelFC06()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_report_id("fc06")

        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                return make_response(model.as_dict())


class FC06ItemsService(MethodView):
    decorators = [catch_errors]

    def get(self, year):
        from api_v2.loggers import logger

        logger.debug(f"{__name__} {year}")
        with repo() as db:
            lista = Informe06ItemsScript(db).fetch_all(year=year)

            return make_response(lista)
