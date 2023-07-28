from flask import Flask
from api import cloud_run

app = Flask(__name__)

app.register_blueprint(cloud_run)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
