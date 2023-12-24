import os
from flask import Flask
from flask_cors import CORS

from core.encoder import CustomJsonEncoder
from logs import logger




app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
CORS(app)


app.json_encoder = CustomJsonEncoder

# @app.before_first_request
# def before_first_request():
#     logger.debug("Verificando modelos")
#     models = ModelBase.__subclasses__()
#     logger.debug(f"modelos encontrados: {models}")
#     check_models_requirements(models)



# def check_models_requirements(models):
#     """Check if the models are created in the database, if not, create them."""
#     with repo() as db:
#         transaction = db.get_session().begin()
#         try:
#             for mdl in models:
#                 logger.debug(f"checking model {mdl.__tablename__}")
#                 if not db.table_exists(mdl):
#                     db.create_table(mdl)
#                     logger.debug(f"(OK) created table {mdl.__tablename__}")
#                 else:
#                     logger.debug(f"(OK) table {mdl.__tablename__} exists")
#         except Exception as ex:
#             transaction.rollback()
#             logger.error(f"error checking models {ex}")
#         else:
#             transaction.commit()
#             logger.success("models checked successfully")



from services_info.routes import *
