"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        "index.html",
        year=datetime.now().year
     )

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template(
        "register.html",
        year=datetime.now().year
     )


@app.route('/login',  methods=['GET', 'POST'])
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        year=datetime.now().year
    )

@app.route('/data',  methods=['GET', 'POST'])
def data():
    """Renders the data page."""
    return render_template(
        'data.html',
        year=datetime.now().year,
        message='Enter Data'
    )