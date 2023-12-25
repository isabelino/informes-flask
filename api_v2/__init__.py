from flask import *

from api_v2.apitest import Prueba
from api_v2.contadores import ContadoresService, ContadorService, ContadorLastIdService
from api_v2.fc03 import FC03Service, FC03ByDateService
from api_v2.fc04 import FC04Service
from api_v2.fc05 import FC05Service, FC05ByDateService, FC05ItemsService
from api_v2.fc06 import FC06Service, FC06ItemsService
from api_v2.fc10 import FC10Service, FC10ListService

api_v2 = Blueprint('api_v2', __name__)

# registro de rutas
api_v2.add_url_rule('/v2/test', view_func=Prueba.as_view('test'))
api_v2.add_url_rule('/v2/contadores/<id>', view_func=ContadorService.as_view('contador_api'))
api_v2.add_url_rule('/v2/contadores', view_func=ContadoresService.as_view('contadores_api'))
api_v2.add_url_rule('/v2/contadores/last/<name>', view_func=ContadorLastIdService.as_view('contador_last_api'))
api_v2.add_url_rule('/v2/fc03', view_func=FC03Service.as_view('fc03'))
api_v2.add_url_rule('/v2/fc03/date/<date>', view_func=FC03ByDateService.as_view('fc03_by_date'))
api_v2.add_url_rule('/v2/fc04', view_func=FC04Service.as_view('fc04'))
api_v2.add_url_rule('/v2/fc05', view_func=FC05Service.as_view('fc05'))
api_v2.add_url_rule('/v2/fc05/date/<date>', view_func=FC05ByDateService.as_view('fc05_by_date'))
api_v2.add_url_rule('/v2/fc05/items/<month>/<year>', view_func=FC05ItemsService.as_view('fc05_items'))
api_v2.add_url_rule('/v2/fc06', view_func=FC06Service.as_view('fc06'))
api_v2.add_url_rule('/v2/fc06/items/<year>', view_func=FC06ItemsService.as_view('fc06_year'))
api_v2.add_url_rule('/v2/fc10', view_func=FC10Service.as_view('fc10'))
api_v2.add_url_rule('/v2/fc10/all', view_func=FC10ListService.as_view('fc10_list'))
