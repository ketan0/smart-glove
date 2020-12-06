#!/usr/bin/env python3
import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scopes = 'user-library-read user-read-playback-state user-modify-playback-state'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes, open_browser=False))

def toggle_playback():
    playback_info = sp.current_playback()
    # TODO: provide a default device id if none is active
    if playback_info:
        sp.pause_playback() if playback_info['is_playing'] else sp.start_playback()

def add_current_song_to_playlist(playlist_id):
    playback_info = sp.current_playback()
    if playback_info:
        sp.playlist_add_items(playlist_id, [playback_info['item']['uri']])

def next_track():
    sp.next_track()

def prev_track():
    sp.previous_track()


# import os

# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])
