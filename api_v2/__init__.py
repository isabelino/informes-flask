from flask import *

from api_v2.apitest import Prueba
from api_v2.contadores import ContadoresService, ContadorService, ContadorLastIdService
from api_v2.fc03 import FC03Service, FC03ByDateService, FC03ListService
from api_v2.fc04 import FC04Service, FC04ListService, FC04ItemsService
from api_v2.fc05 import FC05Service, FC05ByDateService, FC05ItemsService, FC05ListService
from api_v2.fc06 import FC06Service, FC06ItemsService
from api_v2.fc10 import FC10Service, FC10ListService
from api_v2.movements import MovementsService
from api_v2.status import StatusService

api_v2 = Blueprint('api_v2', __name__)

# registro de rutas
api_v2.add_url_rule('/test', view_func=Prueba.as_view('test'))

# [contador]------------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/contador/<name>', view_func=ContadorService.as_view('contador_api'))
api_v2.add_url_rule('/contadores', view_func=ContadoresService.as_view('contadores_api'))

# [fc03]----------------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/fc03/new', view_func=FC03Service.as_view('fc03'))
api_v2.add_url_rule('/fc03/all', view_func=FC03ListService.as_view('fc03_all'))
api_v2.add_url_rule('/fc03/date/<date>', view_func=FC03ByDateService.as_view('fc03_by_date'))

# [fc04]----------------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/fc04/new', view_func=FC04Service.as_view('fc04_new'))
api_v2.add_url_rule('/fc04/items', view_func=FC04ItemsService.as_view('fc04_items'))
api_v2.add_url_rule('/fc04/all', view_func=FC04ListService.as_view('fc04_all'))

# [fc05]----------------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/fc05/new', view_func=FC05Service.as_view('fc05'))
api_v2.add_url_rule('/fc05/all', view_func=FC05ListService.as_view('fc05_all'))
api_v2.add_url_rule('/fc05/date/<date>', view_func=FC05ByDateService.as_view('fc05_by_date'))
api_v2.add_url_rule('/fc05/items/<month>/<year>', view_func=FC05ItemsService.as_view('fc05_items'))

# [fc06]----------------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/fc06/new', view_func=FC06Service.as_view('fc06'))
api_v2.add_url_rule('/fc06/items/<year>', view_func=FC06ItemsService.as_view('fc06_year'))

# [fc10]----------------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/fc10/new', view_func=FC10Service.as_view('fc10'))
api_v2.add_url_rule('/fc10/all', view_func=FC10ListService.as_view('fc10_list'))
# api_v2.add_url_rule('/fc10/items')

# [movements]-----------------------------------------------------------------------------------------------------------
api_v2.add_url_rule('/update/<int:id>', view_func=MovementsService.as_view('contador_update'))
api_v2.add_url_rule('/delete/<int:id>', view_func=MovementsService.as_view('contador_delete'))

api_v2.add_url_rule('/status', view_func=StatusService.as_view('status_service'))
