"""
The flask application package.
"""

from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
"""from flask_wtf import FlaskForm"""
import sqlalchemy
import flask_sqlalchemy
"""from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired"""
from flask_sqlalchemy import SQLAlchemy


import FlaskWebProject1.views

app.config['SECRET_KEY'] = 'Vwvx7NXGMp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class user(db.Model):
    id = db.column(db.Integer, primary_key=True)
    email = db.Column(db.Varchar(50), unique=True, nullable=False)
    password = db.Column(db.Varchar(50), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

