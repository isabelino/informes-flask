from flask.views import MethodView
from sqlalchemy.exc import DatabaseError

from api_v2.conexion import repo_session
from api_v2.models import ModelFC03
from core.decorators import catch_errors
from core.responses import make_response


class FC03Service(MethodView):
    decorators = [catch_errors]

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC03).all()
            return make_response([item.as_dict() for item in lista])

    def post(self):
        data = request.get_json()
        model = ModelFC03()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_id("fc03")

        with repo_session() as s:
            try:
                s.add(model)
            except DatabaseError as e:
                s.rollback()
                return make_response(e, 400)
            else:
                s.commit()
                return make_response(model.as_dict())


class FC03ByDateService(MethodView):
    decorators = [catch_errors]

    def get(self, date):
        with repo_session() as s:
            list = s.query(ModelFC03).filter(ModelFC03.fecha == date).all()
            return make_response([item.as_dict() for item in list])
