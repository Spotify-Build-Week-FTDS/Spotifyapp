'''
Main application/routing file for Spotify Song Suggester
'''

from os import getenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from .models import DB

# Creating a Flask App instance

# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])


def create_app():
    '''
    Creates & configures a flask application instance
    '''
    # Name points to where our path is once we run our code
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    DB.init_app(app)

    # Establishing our base route function with Flask's decorator
    @app.route('/')
    def root():
        return render_template("index.html", title="Home", )

    # Function for refreshing our site
    @app.route('/refresh')
    def refresh():
        DB.drop_all()
        DB.create_all()
        return render_template("index.html", title="Song Suggester has been refreshed!", )

    return app




# TODO: get jinja2 tags in html in order to render app routes
# TODO: generate model classes with features from csv file
# TODO: API call to frontend
# TODO: Routes we need: /, /refresh, /user submissions, 
# TODO: Fixing index.html to replace pig latin
# TODO: Deploy our dummy/skeleton model to Heroku. Make sure we all know how to do git push & pull requests. That means I should setup Heroku with added members, considering I have my student account enabled. Unless Mike would like to handle that? 

# TODO: Stretch Goal: Add in explicit content and genre objects to filter songs. Can achieve this with: ExplicitContentSettingsObject in the spotify dev documentation