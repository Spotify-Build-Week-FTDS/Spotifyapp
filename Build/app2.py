import os
import dotenv 
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import requests
import pandas as pd
from sklearn.preprocessing import StandardScaler
import math


cid = os.getenv('CID')
secret = os.getenv('SECRET')
client_id = cid
client_secret = secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API"""


def get_track_id(artist, track):
    track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    list_of_lists = track_id['tracks']['items']
    song_list_meta = (list_of_lists[0])
    for k , v in song_list_meta.items():
        if k == 'id':
           return k, v
   

def get_data(cid, secret, track_id):
    # Post
    Auth_Url = 'https://accounts.spotify.com/api/token'
    auth_response = requests.post(Auth_Url, {
        'grant_type' : 'client_credentials',
        'client_id' : cid,
        'client_secret' : secret
    })

    auth_response_data = auth_response.json()
    acess_token = auth_response_data['access_token']
    headers = {
        'Authorization': 'Bearer {token}'.format(token=acess_token)
    }

    Base_URL = 'https://api.spotify.com/v1/'
    track_id = track_id
    r = requests.get(Base_URL + 'audio-features/' + track_id, headers=headers)
    r = r.json()
    return(r)

def convert(g):
    g_list = list(g.values())
    key_list = list(g.keys())
    input_array = pd.DataFrame(g_list)
    column_names = (key_list)
    input_array = (input_array.T)
    input_array.columns = column_names
    return input_array

def transform_array(x):
    std_sca = StandardScaler()
    x['album_id'] = "null"
    x['artist_ids'] = 'null'
    x['explicit'] = 0
    x['Key_0'] = 1
    x['Key_1'] = 0
    x['Key_2'] = 0
    x['Key_3'] = 0
    x['Key_4'] = 0
    x['Key_5'] = 0
    x['Key_6'] = 0
    x['Key_7'] = 0
    x['Key_8'] = 0
    x['Key_9'] = 0
    x['Key_10'] = 0
    x['Key_11'] = 0
    x['Key_12'] = 0
    x['Free_sig'] = 0
    x['1_sig'] = 0
    x['2_sig'] = 0
    x['3_sig'] = 0
    x['4_sig'] = 1
    x['years_old'] = 7
    #rearragne
    x = x[['album_id', 'artist_ids', 'explicit','danceability', 'energy', 'loudness', 'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness', 'valence', 'tempo', 'duration_ms','years_old', 'Key_0',
    'Key_1', 'Key_2', 'Key_3', 'Key_4', 'Key_5', 'Key_6', 'Key_7', 'Key_8','Key_9', 'Key_10', 'Key_11', 'Free_sig', '1_sig', '2_sig', '3_sig',
    '4_sig']]

    #using Standard Scalar for dataset 
    x['danceability'] = (x['danceability'][0] - 0.49305652) / math.sqrt(0.03597445)
    x['energy'] = (x['energy'][0] - 0.50953629) / math.sqrt(0.08683854)
    x['speechiness'] = (x['speechiness'][0] - 0.08438219) / math.sqrt(0.01345399)
    x['acousticness'] = (x['acousticness'][0] - 0.4467511) / math.sqrt(0.14838001)
    x['instrumentalness'] = (x['instrumentalness'][0] - 0.28286054) / math.sqrt(0.14158983)
    x['liveness'] = (x['liveness'][0] - 0.20159939) / math.sqrt(0.03256545)
    x['valence'] = (x['valence'][0] - 0.42798662) / math.sqrt(0.07316183)
    x['tempo'] = (x['tempo'][0] - 117.63435181) / math.sqrt(957.10006119)
    x['duration_ms'] = (x['duration_ms'][0] - 248839.86096219) / math.sqrt(2.63121781e+10) 
    x['years_old'] = (x['years_old'][0] - 13.6554241) / math.sqrt(112.97315674)

    return x
