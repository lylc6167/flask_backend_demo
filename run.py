from flask_app import app
from config import web


if __name__ == '__main__':
    # 0.0.0.0:8080
    app.run(host=web['ip'], port=web['port'])