from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, flash, redirect, jsonify

from flask_login import login_user, LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = "Ntf64RDSLYBgbUY8KzvCBdhEnmd2VEY8nU8"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

socketio = SocketIO(app)
db = SQLAlchemy(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signin_html')
def open_signin():
	return render_template('signin.html')

@app.route('/login_html')
def open_login():
	return render_template('login.html')


from forum.routes import *
from forum.templates import *

