import datetime

from flask import request
from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo_session
from api_v2.models import ModelFC03
from core.decorators import catch_errors
from core.generators import last_report_id
from core.responses import make_response
from .loggers import logger


class FC03Service(MethodView):
    decorators = [catch_errors]

    def post(self):
        logger.debug("Obtiene la lista de FC03")
        data = request.get_json()
        logger.debug(data)
        model = ModelFC03()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_report_id("fc03")
        logger.warning(f'generado numero {model.numero}', extra=model.as_dict())
        # model.items = [{'cuenta': '26112', 'subcuenta': '1', 'analitico1': '9', 'analitico2': '99',
        #                 'descripcion': "Muebles y enseres \nmobiliarios y enseres de oficina \nEscritorios \notros tipos de escritorio\nMESA DE MADERA CLASSIC MOBLES {10643}",
        #                 'fecha_adquisicion': '20-12-2018', 'rotulado': '18-6-3-1224', 'cantidad': '1',
        #                 'valor_unitario': '363.636', 'valor_total': '363.636', 'bienes': '',
        #                 'estado_conservacion': 'B.', 'diferencia_libro': '', 'observacion': ''},
        #                {'cuenta': '26112', 'subcuenta': '1', 'analitico1': '9', 'analitico2': '99',
        #                 'descripcion': "Muebles y enseres \nmobiliarios y enseres de oficina \nEscritorios \notros tipos de escritorio\nMESA DE MADERA CLASSIC MOBLES {10643}",
        #                 'fecha_adquisicion': '20-12-2018', 'rotulado': '18-6-3-1224', 'cantidad': '1',
        #                 'valor_unitario': '363.636', 'valor_total': '363.636', 'bienes': '',
        #                 'estado_conservacion': 'B.', 'diferencia_libro': '', 'observacion': ''},
        #                {'cuenta': '26112', 'subcuenta': '1', 'analitico1': '9', 'analitico2': '99',
        #                 'descripcion': "Muebles y enseres \nmobiliarios y enseres de oficina \nEscritorios \notros tipos de escritorio\nMESA DE MADERA CLASSIC MOBLES {10643}",
        #                 'fecha_adquisicion': '20-12-2018', 'rotulado': '18-6-3-1224', 'cantidad': '1',
        #                 'valor_unitario': '363.636', 'valor_total': '363.636', 'bienes': '',
        #                 'estado_conservacion': 'B.', 'diferencia_libro': '', 'observacion': ''}
        #                ]

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


class FC03ListService(MethodView):
    decorators = [catch_errors]
    """
    Obtiene la lista de FC03
    """

    def get(self):
        logger.debug("Obtiene la lista de FC03")
        with repo_session() as s:
            lista = s.query(ModelFC03).order_by(ModelFC03.id.desc()).all()

            return make_response(lista)


class FC03ByDateService(MethodView):
    decorators = [catch_errors]

    def get(self, date):
        with repo_session() as s:
            list = s.query(ModelFC03).filter(ModelFC03.fecha == date).all()
            return make_response([item.as_dict() for item in list])
