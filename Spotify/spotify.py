'''
Handles Connections To Spotify Database
'''

from os import getenv
import spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

# Aunthentication for use of Spotify's API
# Using .env file to assign client ID & Cl
SPOTIFY_CLIENT_ID = getenv('CLIENT_ID')
SPOTIFY_CLIENT_KEY_SECRET = getenv('CLIENT_SECRET')

# This method sends requests to Spotify's API with out client ID & client key secret(basically a username & 
# password) and returns an authentication object, essentially validating a login.
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(SPOTIFY_CLIENT_ID,
                                                           SPOTIFY_CLIENT_KEY_SECRET))


df = pd.read_csv("")
conn = 






