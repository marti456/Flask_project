from datetime import datetime
from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)

from forum import app, db
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    topic = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now())

db.create_all()