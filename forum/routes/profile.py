import json
import os

from flask import render_template, request, flash, redirect, jsonify

from forum import app, db
from forum.models import User
from forum.utils import random_string, stop_logged_users


@app.route('/signin', methods=['GET', 'POST'])
@stop_logged_users
def sign():
    if request.method == 'GET':
        return render_template('signin.html')
    else:
        username = request.form['username']
        password = request.form['password']

        try:
            user = User(
                    username=username,
                    password=password,
                    )
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            flash('Error: {}'.format(e))
            return redirect(request.url)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        info = json.loads(request.data)
        username = info.get('username', 'guest')
        password = info.get('password', '') 
        user = User.objects(name=username,
                        password=password).first()
        if user:
            login_user(user)
            return jsonify(user.to_json())
        else:
            return jsonify({"status": 401, "reason": "Username or Password Error"})

