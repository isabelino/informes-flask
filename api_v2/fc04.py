import datetime

from flask import request
from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.loggers import logger
from api_v2.models import ModelFC04
from core.generators import last_id
from core.responses import make_response


class FC04Service(MethodView):

    def post(self):
        logger.debug("Obtiene la lista de FC04")
        data = request.get_json()
        logger.warning(data)

        model = ModelFC04()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_id("fc04")
        logger.debug(model.as_dict())
        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                return make_response(model.as_dict())


class FC04ItemsService(MethodView):
    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC04.items).order_by(ModelFC04.id.desc()).all()
            return make_response(lista)


class FC04ListService(MethodView):
    def get(self):
        """
        Obtiene la lista de FC04
        :return:
        """
        with repo_session() as s:
            lista = s.query(ModelFC04).all()
        return make_response(lista)
