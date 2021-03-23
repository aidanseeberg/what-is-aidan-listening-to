import pylast
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json


### LAST.FM AUTHENTICATION
last_key = "SECRET"
last_secret = "SECRET"

lastfm = pylast.LastFMNetwork(last_key,last_secret)

### SPOTIFY AUTHENTICATION
client_id = "SECRET"
client_secret = "SECRET"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id, client_secret))


### INITIAL REQUESTS
aidan = lastfm.get_user("YOUR_USERNAME")


### PERIOD
'''
PERIOD_OVERALL = "overall"
PERIOD_7DAYS = "7day"
PERIOD_1MONTH = "1month"
PERIOD_3MONTHS = "3months"
PERIOD_6MONTHS = "6months"
PERIOD_12MONTHS = "1year"
'''

limit = 5


### SPOTIFY REQUESTS
def get_track_link(artist, track):
    return spotify.search(q=artist + " " + track,type='track',limit=1)['tracks']['items'][0]['external_urls']['spotify']

def get_artist_link(artist):
    return spotify.search(q=artist,type='artist',limit=1)['artists']['items'][0]['external_urls']['spotify']

### CREATING REPORT
def get_now_playing():

    try: 
        now_playing = aidan.get_now_playing()
        artist = now_playing.artist.get_name()
        track = now_playing.get_name()
        return [str(artist + " - " + track), get_track_link(artist,track)]
    except:
        return ("Nothing currently...","")

def get_recent_tracks():
    recent = aidan.get_recent_tracks(limit=limit)
    recent_list = []

    for item in recent:
        artist = item.track.artist.get_name()
        track = item.track.get_name()
        recent_list.append([str(artist) + " - " + str(track),get_track_link(artist,track)])
    
    return recent_list

def get_top_tracks(period):
    top_tracks = aidan.get_top_tracks(period=period,limit=limit)
    top_list = []

    for item in top_tracks:
        artist = item.item.artist.get_name()
        track = item.item.get_name()
        top_list.append([str(track), get_track_link(artist,track)])

    print('here done')
    return top_list

def get_top_artists(period):
    top_artists = aidan.get_top_artists(period=period,limit=limit)
    top_list = []

    for item in top_artists:
        name = item.item.get_name()
        top_list.append([name,get_artist_link(name)])
    
    return top_list

def get_period_string(period):
    if period == '7day':
        return 'week'
    elif period == '1month':
        return 'month'
    elif period == '3months':
        return '3 months'
    elif period == '6months':
        return '6 months'
    elif period == '1year':
        return 'year'
    else: return '0 seconds'




### SUMMARY
report_json = ''
report = dict()

def generate_report(period):
    print('------------------------------------')

    report['now'] = get_now_playing()
    report['recent'] = get_recent_tracks()

    report['tracks'] = get_top_tracks(period)

    report['artists'] = get_top_artists(period)
    
    report['period'] = get_period_string(period)

    report_json = json.dumps(report)

    print(json.dumps(report))
    print('------------------------------------')
    print("report for " + period + " completed.")


