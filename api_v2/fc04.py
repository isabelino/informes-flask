import datetime
import json

from flask import request
from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo_session
from api_v2.loggers import logger
from api_v2.models import ModelFC04
from core.decorators import catch_errors
from core.generators import last_report_id, set_report_id
from core.responses import make_response


class FC04Service(MethodView):
    decorators = [catch_errors]

    def post(self):
        logger.debug("Obtiene la lista de FC04")
        data = request.get_json()
        logger.warning(data)

        report_id = last_report_id("fc04")

        model = ModelFC04()
        model.from_dict(data)
        model.nro_informe = report_id
        model.fecha = datetime.date.today()
        model.cont_informe = model.nro_informe
        # establecer el siguiente numero de reporte
        set_report_id("fc04", report_id + 1)

        items = [{'cuenta': '26112',
                  'subcuenta': '\n 03',
                  'analitico1': '\n \n 99',
                  'analitico2': '04',
                  'descripcion': "Muebles y enseres \nequipos de eseo y seguridad\nOtros equipos y mubles de AHS\nOtros tipos de enceradoras electricas\nAPARATO DIFUSOR SPHIRUS{11648}",
                  'fecha_adquisicion': '01-10-2019',
                  'tipo': 'factura',
                  'nro': '01',
                  'rotulado': '18-6-3-1224',
                  'cantidad': '1',
                  'valor_unitario': '59.091',
                  'valor_total': '59.091',
                  'signo': 'signo',
                  'fecha_incorp': '10-10-2019',
                  'vida_util': '10',
                  'origen_movimento': 'C'},
                 {'cuenta': '26112',
                  'subcuenta': '\n 03',
                  'analitico1': '\n \n 99',
                  'analitico2': '04',
                  'descripcion': "Muebles y enseres \nequipos de eseo y seguridad\nOtros equipos y mubles de AHS\nOtros tipos de enceradoras electricas\nAPARATO DIFUSOR SPHIRUS{11648}",
                  'fecha_adquisicion': '01-10-2019',
                  'tipo': 'factura',
                  'nro': '01',
                  'rotulado': '18-6-3-1224',
                  'cantidad': '1',
                  'valor_unitario': '59.091',
                  'valor_total': '59.091',
                  'signo': 'signo',
                  'fecha_incorp': '10-10-2019',
                  'vida_util': '10',
                  'origen_movimento': 'C'}
                 ]
        model.items = json.dumps(items)

        logger.debug(model.as_dict())
        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                logger.success(model.as_dict())
                set_report_id("fc04", report_id + 1)
                return make_response(model.as_dict())


class FC04ItemsService(MethodView):
    decorators = [catch_errors]

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC04.items).order_by(ModelFC04.id.desc()).all()
            return make_response(lista)


class FC04ListService(MethodView):
    decorators = [catch_errors]

    def get(self):
        """
        Obtiene la lista de FC04
        :return:
        """
        with repo_session() as s:
            lista = s.query(ModelFC04).all()
        return make_response(lista)
