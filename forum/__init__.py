from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/dev.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "Ntf64RDSLYBgbUY8KzvCBdhEnmd2VEY8nU8"

socketio = SocketIO(app)
db = SQLAlchemy(app)

from forum.routes import *
from forum.templates import *

