from flask.views import MethodView

from api_v2.loggers import logger
from core.decorators import catch_errors
from core.generators import last_report_id
from core.responses import make_response


class ContadorService(MethodView):
    """
    Servicio para contador
    """
    decorators = [catch_errors]

    def get(self, name: str):
        logger.debug(f'Obtiene el contador {name}')
        contador = last_report_id(name)
        return make_response(contador)

# class ContadorLastIdService(MethodView):
#     """
#     Servicio para contador
#     """
#     decorators = [catch_errors]
#
#     def get(self, name: str):
#         with repo_session() as s:
#             contador = s.query(ModelContadores) \
#                 .filter_by(informe=name) \
#                 .order_by(desc_op(ModelContadores.numero)).limit(1).one_or_none()
#
#             return make_response(contador)
#
#     def post(self, name):
#         contador = next_report_id(name)
#         return make_response(contador)


# class ContadoresService(MethodView):
#     """
#     Servicio para contadores
#     """
#     decorators = [catch_errors]
#
#     def get(self):
#         with repo_session() as s:
#             contadores = s.query(ModelContadores).order_by(desc_op(ModelContadores.id)).all()
#             return make_response([item.as_dict() for item in contadores])
#
#     def post(self):
#         model = ModelContadores()
#         model.from_dict(request.get_json())
#         model.fecha = datetime.date.today().isoformat()
#
#         with repo_session() as s:
#             model.numero = last_report_id(model.informe)
#
#             s.add(model)
#             s.commit()
#             return make_response(model)
