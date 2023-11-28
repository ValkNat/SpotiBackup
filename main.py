import spotipy
import output
from spotipy.oauth2 import SpotifyClientCredentials
import userplaylists

#create spotify dev app on the developer portal to access these
client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR CLIENT SECRET'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_url):
    playlist_id = playlist_url.split('/')[-1]

    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    song_list = []

    for track in tracks:
        track_info = track['track']
        song_name = track_info['name']

        artist_name = track_info['artists'][0]['name']
        song_list.append(f'{song_name} - {artist_name}')

    return song_list


if __name__ == '__main__':
    print("Please enter your user url: ")
    user_url = input()
    playlist_dictionary = userplaylists.scrape_spotify_playlists(user_url)
    print(playlist_dictionary)

    for playlist_name, playlist_url in playlist_dictionary.items():
        song_list = get_playlist_tracks(playlist_url)
        output.write_playlist_name_to_file(playlist_name)
        output.output_to_file(song_list)

