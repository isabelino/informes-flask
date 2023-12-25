from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelFC04
from core.responses import make_response


class FC04Service(MethodView):

    def get(self):
        with repo_session() as s:
            lista = s.query(ModelFC04).all()
            return make_response([item.as_dict() for item in lista])

    def post(self):
        data = request.get_json()
        model = ModelFC04()
        model.from_dict(data)
        model.fecha = datetime.date.today().isoformat()
        model.numero = last_id("fc04")
