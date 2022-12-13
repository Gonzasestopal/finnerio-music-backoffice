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


@blueprint.route('/genres/<genre_id>/artists')
def artist_by_genre(genre_id):
    path = '/'.join(['genres', genre_id, 'artists'])
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/artists.html', artists=info)

@blueprint.route('/artists')
def artists():
    path = 'artists'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/artists.html', artists=info)

@blueprint.route('/albums')
def albums():
    path = 'albums'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/albums.html', albums=info)

@blueprint.route('/artists/<artist_id>/albums')
def albums_by_artist(artist_id):
    path = '/'.join(['artists', artist_id, 'albums'])
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/albums.html', albums=info)

@blueprint.route('/albums/<album_id>')
def songs_by_album(album_id):
    path = '/'.join(['albums', album_id])
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/songs.html', songs=info)

@blueprint.route('/songs')
def song_by_artist():
    path = 'songs'
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/songs.html', songs=info)


@blueprint.route('/artists/<artist_id>')
def find_artist(artist_id):
    path = '/'.join(['artists', artist_id])
    response = requests.get(urljoin(FINNERIO_MUSIC_API_URL, path))
    info = response.json()
    return render_template('pages/artists.html', artists=info)


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
