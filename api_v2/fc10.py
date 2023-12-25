from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelFC10
from core.responses import make_response


class FC10Service(MethodView):

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        model = ModelFC10()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_id("fc10")

        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                return make_response(model.as_dict())


class FC10ListService(MethodView):
    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC10).all()
        return make_response([item.as_dict() for item in lista])
