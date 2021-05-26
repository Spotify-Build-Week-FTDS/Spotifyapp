'''
SQLAlchemy Models & DB Architecture
'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Creating Spotify Table
class Spotify(db.Model):
    id = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(120), nullable=False)
    album = db.Column(db.String(120), nullable=False)
    album_id = db.Column(db.String(30), nullable=False)
    artists = db.Column(db.String(120), nullable=False)
    artist_ids = db.Column(db.String(30), nullable=False)
    explicit = db.Column(db.Integer, primary_key=True)
    danceability = db.Column(db.Float, nullable=False)
    energy = db.Column(db.Float, nullable=False)
    key = db.Column(db.Float, nullable=False)
    loudness = db.Column(db.Float, nullable=False)
    mode = db.Column(db.Float, nullable=False)
    speechiness = db.Column(db.Float, nullable=False)
    acousticness = db.Column(db.Float, nullable=False)
    instrumentalness = db.Column(db.Float, nullable=False)
    liveness = db.Column(db.Float, nullable=False)
    valence = db.Column(db.Float, nullable=False)
    tempo = db.Column(db.Float, nullable=False)
    time_signature = db.Column(db.Float, nullable=False)
    years_old = db.Column(db.Float, nullable=False)
    release_date = db.Column(db.)
    Key_0 = db.Column(db.Integer, primary_key=True)
    Key_1 = db.Column(db.Integer, primary_key=True)
    Key_2 = db.Column(db.Integer, primary_key=True)
    Key_3 = db.Column(db.Integer, primary_key=True)
    Key_4 = db.Column(db.Integer, primary_key=True)
    Key_5 = db.Column(db.Integer, primary_key=True)
    Key_6 = db.Column(db.Integer, primary_key=True)
    Key_7 = db.Column(db.Integer, primary_key=True)
    Key_8 = db.Column(db.Integer, primary_key=True)
    Key_9 = db.Column(db.Integer, primary_key=True)
    Key_10 = db.Column(db.Integer, primary_key=True)
    Key_11 = db.Column(db.Integer, primary_key=True)
    Free_sig = db.Column(db.Integer, primary_key=True)
    1_sig = db.Column(db.Integer, primary_key=True)
    2_sig = db.Column(db.Integer, primary_key=True)
    3_sig = db.Column(db.Integer, primary_key=True)
    4_sig = db.Column(db.Integer, primary_key=True)

    # Representation of our Class
    def __repr__(self):
        return f"<Spotify: {self.name}>"

# TODO: Use .dtypes on the dataframe in colab on the release date column to see if it's a string, date, or datetime type so I can add it
#TODO: Figure out if nested rows in 'artists' & 'artist_ids' will pose a problem