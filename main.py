import os
from dotenv import load_dotenv
from services_info import app, Routes
from flask_swagger_ui import get_swaggerui_blueprint

load_dotenv()  # load .env file to environment

routes = Routes(app)  # load routes

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config = {
        'app_name': "informes-senave"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
