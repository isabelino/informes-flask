import os

from flask.views import MethodView
from tcppinglib import tcpping

from core.responses import make_response


class StatusService(MethodView):
    def get(self):
        hosts = {}

        database = tcpping(os.getenv('DATABASE_HOST'), 3306, 3).is_alive
        frontend = tcpping(os.getenv('FRONTEND_HOST'), 8080, 3).is_alive
        pma = tcpping(os.getenv('PMA_HOST'), 8081, 3).is_alive

        hosts.update({'database': 1 if database else 0,
                      'frontend': 1 if frontend else 0,
                      'pma': 1 if pma else 0
                      })

        return make_response(hosts)
