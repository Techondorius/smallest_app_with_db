import sys
sys.dont_write_bytecode = True

from flask import Flask, Blueprint
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from blueprints import db_connection

app = Flask(__name__)
CORS(app)

app.register_blueprint(db_connection.app, url_prefix='/noot')

# DB設定
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///Test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO']=False
db = SQLAlchemy(app)

# Model定義
class ToDoItem(db.Model):
    __tablename__ = "todoitems"
    item_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    done = db.Column(db.Boolean, nullable=False, default=False)

@app.before_first_request
def init():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)