from flask import render_template, Blueprint, request
from app.forms import *

blueprint = Blueprint('pages', __name__)

import requests

################
#### routes ####
################


@blueprint.route('/')
def home():
    response = requests.get("http://localhost:8000/genres")
    genres_info = response.json()
    return render_template('pages/placeholder.home.html', genres=genres_info)


@blueprint.route('/about')
def about():
    return render_template('pages/placeholder.about.html')


@blueprint.route('/login')
def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)


@blueprint.route('/register')
def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)


@blueprint.route('/forgot')
def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)
