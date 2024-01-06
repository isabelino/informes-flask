from flask import request
from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelMovement
from core.decorators import catch_errors
from core.responses import make_response


class MovementsService(MethodView):
    decorators = [catch_errors]

    def put(self):
        data = request.get_json()
        with repo_session() as s:
            model = s.query(ModelMovement).filter(ModelMovement.id == data['id']).one_or_none()
            if model:
                model.date = data['date']
                model.description = data['description']
                model.quantity = data['quantity']
                s.commit()
                return make_response("OK")
            else:
                return make_response("No se encuentra el registro a actualizar", 400)

    def delete(self):
        data = request.get_json()
        with repo_session() as s:
            model = s.query(ModelMovement).filter(ModelMovement.id == data['id']).one_or_none()
            if model:
                s.delete(model)
                s.commit()
                return make_response("OK")
            else:
                return make_response("No se encuentra el registro a eliminar", 400)
