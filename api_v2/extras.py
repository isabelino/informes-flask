import datetime

from flask.views import MethodView

from api_v2.conexion import repo_session
from api_v2.models import ModelContadores
from core.decorators import catch_errors
from core.responses import make_response


class ExtraYearServices(MethodView):
    decorators = [catch_errors]

    def get(self, report):
        from api_v2.loggers import logger

        # SELECT strftime("%Y", fecha) as year from contadores WHERE informe="{num}" ORDER BY id DESC LIMIT 1;

        with repo_session() as s:
            year = s.query(ModelContadores.fecha) \
                .filter_by(informe=report) \
                .order_by(ModelContadores.id.desc()) \
                .limit(1) \
                .scalar()

            if not year:
                year = datetime.date.today().year

        logger.debug(f"{report}: {year}")

        return make_response(year)
