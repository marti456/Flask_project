import hashlib
import string
import random

from functools import wraps
from flask import request, flash, redirect

from itsdangerous import (TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired)


from forum import app


def require_login(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if not token or not verify_token(token):
            flash('You have to be logged in to access this page')
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper


def stop_logged_users(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if token and verify_token(token):
            flash('You\'re already logged in.')
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))

