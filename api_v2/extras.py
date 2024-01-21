from flask.views import MethodView


class ExtraYearServices(MethodView):
    def get(self, num):
        ...
