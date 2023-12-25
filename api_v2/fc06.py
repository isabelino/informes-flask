from flask.views import MethodView

from api_v2.conexion import repo, repo_session
from api_v2.scripts import Informe06ItemsScript
from core.decorators import catch_errors


class FC06Service(MethodView):
    decorators = [catch_errors]

    def get(self):
        pass

    def post(self):
        data = request.get_json()
        model = ModelFC06()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_id("fc06")

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

    def get(self, year: int):
        with repo() as db:
            lista = Informe06ItemsScript().execute(db, year=year).fetch_all()

        return make_response([item.as_dict() for item in lista])
