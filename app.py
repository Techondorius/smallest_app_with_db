import sys
sys.dont_write_bytecode = True

from flask import Flask, Blueprint
from flask_cors import CORS

from blueprints import db_connection

app = Flask(__name__)
CORS(app)

app.register_blueprint(db_connection.app, url_prefix='/noot')

if __name__ == '__main__':
    app.run(debug=True)