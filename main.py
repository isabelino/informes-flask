from dotenv import load_dotenv

from api_v2 import api_v2
from app_cli import AppCli
from services_info import app

load_dotenv()  # load .env file to environment

# deprecated blueprint: dgarcia: 25-01-2024: changed to api_v2
# routes = Routes(app)  # load routes

# registro del blueprint api_v2
app.register_blueprint(api_v2, url_prefix='/api/v2/')

commands = AppCli(app)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True, use_reloader=True)
