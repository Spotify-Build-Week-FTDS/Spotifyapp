from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Track(DB.model):
    id = DB.Column(DB.Integer, primary_key=True)
    name   = DB.Column(DB.String(50), nullable=False)
    track_id = DB.Column(DB.String(50), nullable=False)
    album = DB.Column(DB.String(50), nullable=False)
    artist = DB.Column(DB.String(50), nullable=False)
    
    def __repr__(self):
        return "<Track {}>".format(self.track)
    
class SongCluster:
    def __init__(self, name, album, artists, explicit, danceability,
                 energy, key, loudness, mode, speechiness,
                 acousticness, instrumentalness, duration_ms,
                 tempo, valence):
                    self.name = name
                    self.album = album
                    self.artists = artists
                    self.explicit = explicit
                    self.danceability = danceability
                    self.energy = energy
                    self.key = key
                    self.loudness = loudness
                    self.mode = mode
                    self.speechiness = speechiness
                    self.acousticness = acousticness
                    self.instrumentalness = instrumentalness
                    self.duration_ms = duration_ms
                    self.tempo = tempo
                    self.valence = valence
                    
class Song_NN:
    def __init__(self, acousticness, disc_number, energy, duration_ms,
                 danceability, explicit, instrumentalness, key, tempo, 
                 liveness, loudness, mode, speechiness, time_signature,
                 track_number, valence):
                    self.acousticness = acousticness
                    self.disc_number = disc_number
                    self.energy = energy
                    self.duration_ms = duration_ms
                    self.danceability = danceability
                    self.explicit = explicit
                    self.instrumentalness = instrumentalness
                    self.key = key
                    self.tempo = tempo
                    self.liveness = liveness
                    self.loudness = loudness
                    self.mode = mode
                    self.speechiness = speechiness
                    self.time_signature = time_signature
                    self.track_number = track_number
                    self.valence = valence
                    
                    
class Output:
    def __init__(self, name, artist):
        self.name = name
        self.artist = artist
