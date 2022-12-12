from urllib.parse import urljoin

import requests
from flask import Blueprint, render_template, request

from src.forms import *
from src.settings import FINNERIO_MUSIC_API_URL

blueprint = Blueprint('pages', __name__)




################
#### routes ####
################


@blueprint.route('/')
def genres():
    path = 'genres'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/genres.html', genres=info)


@blueprint.route('/artists')
def artists():
    path = 'genres/1/artists'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/artists.html', artists=info)

@blueprint.route('/albums')
def albums():
    path = 'artists/2/albums'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    print(info)
    return render_template('pages/albums.html', albums=info)

@blueprint.route('/songs')
def songs():
    path = 'albums/3/'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/songs.html', songs=info)


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
