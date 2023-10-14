import os
from dotenv import load_dotenv
from services_info import app, Routes

load_dotenv()  # load .env file to environment

routes = Routes(app)  # load routes


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
