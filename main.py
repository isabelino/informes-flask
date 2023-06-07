import os

from services_info import app, Routes

routes = Routes(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)