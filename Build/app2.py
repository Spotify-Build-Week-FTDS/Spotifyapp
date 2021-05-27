import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access authorised Spotify data
import requests
"""cid = '6d40450899dc48c2b04ea25ef23a0cf0'
secret = '787f733975e64f62ab5463b3e658c613'
client_id = cid
client_secret = secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager) #spotify object to access API


artist= 'Lester Flatt'
track= 'Foggy Mountain Breakdown'"""

def get_track_id(artist, track):
    track_id = sp.search(q='artist:' + artist + ' track:' + track, type='track')
    list_of_lists = track_id['tracks']['items']
    song_list_meta = (list_of_lists[0])
    for k, v in song_list_meta.items():
        if k == 'id':
            return k , v
   

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

"""disc_num, track_id = get_track_id(artist, track)
print(track_id)
print("Function 1 Complete")
response = get_data(cid, secret, track_id)
print(response)
print("Function 2 Complete")
TODO Translate Json file to array of array as was inputed into the DS4 model
TODO Impute, Scale, and OHE array"""
