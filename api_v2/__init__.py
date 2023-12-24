from flask import *

from api_v2.apitest import Prueba
from api_v2.contadores import ContadoresService, ContadorService
from api_v2.fc03 import FC03Service
from api_v2.fc04 import FC04Service
from api_v2.fc05 import FC05Service
from api_v2.fc06 import FC06Service
from api_v2.fc10 import FC10Service

api_v2 = Blueprint('api_v2', __name__)


# registro de rutas
api_v2.add_url_rule('/v2/test', view_func=Prueba.as_view('test'))
api_v2.add_url_rule('/v2/contadores/<id>', view_func=ContadorService.as_view('contador_api'))
api_v2.add_url_rule('/v2/contadores', view_func=ContadoresService.as_view('contadores_api'))
api_v2.add_url_rule('/v2/fc03', view_func=FC03Service.as_view('fc03'))
api_v2.add_url_rule('/v2/fc04', view_func=FC04Service.as_view('fc04'))
api_v2.add_url_rule('/v2/fc05', view_func=FC05Service.as_view('fc05'))
api_v2.add_url_rule('/v2/fc06', view_func=FC06Service.as_view('fc06'))
api_v2.add_url_rule('/v2/fc10', view_func=FC10Service.as_view('fc10'))
