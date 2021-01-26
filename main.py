from flask import Flask
from flask import render_template, request, flash, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://dev.db'
db = SQLAlchemy(app)
db.create_all()

@app.route('/')

def index():
	return render_template('index.html')



@app.route('/handle_data', methods=['POST'])
def handle_data():
    projectpath = request.form['projectFilepath']

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(600), unique=True, nullable=False)