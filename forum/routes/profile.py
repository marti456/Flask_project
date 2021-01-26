import json
import os

from flask import render_template, request, flash, redirect, jsonify

from forum import app, db
from forum.models import User
from forum.utils import allowed_file, random_string, stop_logged_users

@app.route('/signin', methods=['GET', 'POST'])
@stop_logged_users
def register():
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
@stop_logged_users
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        data = json.loads(request.data.decode('ascii'))
        username = data['username']
        password = data['password']

        user = User.query.filter_by(username=username).first()
        if not user or not user.verify_password(password):
            return jsonify({'token': None})
        token = user.generate_token()
        return jsonify({'token': token.decode('ascii')})