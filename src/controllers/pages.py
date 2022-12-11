from flask import render_template, Blueprint, request
from src.forms import *

blueprint = Blueprint('pages', __name__)

from src.settings import FINNERIO_MUSIC_API_URL

from urllib.parse import urljoin

import requests

################
#### routes ####
################


@blueprint.route('/')
def home():
    path = 'genres'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
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
