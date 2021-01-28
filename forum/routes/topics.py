from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

from forum import app, db
from forum.models import Topic
from forum.utils import random_string, require_login

from flask import request, flash, redirect

@require_login
@app.route('/topic', methods=['GET', 'POST'])
def topic():
    if request.method == 'GET':
        return render_template('topic.html')
    else:
        title = request.form['title']
        description = request.form['description']

        try:
            topic = Topic(title=title, description=description)
            db.session.add(topic)
            db.session.commit()
            return redirect('/logged')
        except Exception as e:
            flash('Error: {}'.format(e))
            return redirect('/logged')


@app.route('/logged', methods=['GET', 'POST'])
def logged():
    return render_template('logged.html', topics=Topic.query.all())
