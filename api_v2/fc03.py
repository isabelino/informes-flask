from flask.views import MethodView

from api_v2.models import ModelFC03


class FC03Service(MethodView):

    def get(self):
        with repo() as db:
            return db.get_session().query(ModelFC03).all()
