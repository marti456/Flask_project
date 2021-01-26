import hashlib
import string
import random

from functools import wraps

from flask import request, flash, redirect

from itsdangerous import (
        TimedJSONWebSignatureSerializer as Serialization,
        BadSignature,
        SignatureExpired
)

from forum import app

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def verify_token(token):
    s = Serialization(app.secret_key)
    try:
        s.loads(token)
    except (BadSignature, SignatureExpired):
        return False
    return True

def stop_logged_users(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if token and verify_token(token):
            flash('Вече сте си влезли в профила.')
            return redirect('/')
        return func(*args, **kwargs)
    return wrapper

def random_string(length):
    return ''.join(random.choice(string.ascii_letters) for x in range(length))