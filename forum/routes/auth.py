from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from forum import app, db
from forum.models import User

import hashlib
import string
import random

from flask import request, flash, redirect

#Не съм сигурен дали това ни трябва тук.
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/signin', methods=['GET', 'POST'])
def sign():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()

        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Error: {}'.format(e))
            return redirect('/')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form['username']
        password = hashlib.sha256(request.form['password'].encode('utf-8')).hexdigest()
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            login_user(user)
            return render_template('logged.html')

        return render_template('login.html', username=username, password=password)
