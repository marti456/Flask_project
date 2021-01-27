from flask import Flask, render_template, request, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

import hashlib
import string
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.secret_key = "tarikatcheto"

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)



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

        return render_template('login.html', username = username, password = password)




if __name__ == '__main__':
    db.create_all()

    app.run(debug = True)

