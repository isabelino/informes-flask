from dotenv import load_dotenv
from flask_swagger_ui import get_swaggerui_blueprint

from api_v2 import api_v2
from app_cli import AppCli
from services_info import app, Routes

load_dotenv()  # load .env file to environment

routes = Routes(app)  # load routes

SWAGGER_URL = "/swagger"
API_URL = "/static/swagger.json"

# registro del blueprint api_v2
app.register_blueprint(api_v2, url_prefix='/api')

# registro del blueprint swagger
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "informes-senave"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

commands = AppCli(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, use_reloader=True)
