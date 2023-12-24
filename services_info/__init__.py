import os
from flask import Flask
from flask_cors import CORS

from core.encoder import CustomJsonEncoder
from logs import logger




app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
CORS(app)


app.json_encoder = CustomJsonEncoder



from services_info.routes import *
