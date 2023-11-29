import spotipy
import output
from spotipy.oauth2 import SpotifyClientCredentials
import userplaylists
import tkinter as tk

#tkinter (GUI) setup
app = tk.Tk()
app.title("SpotiBackup")

client_id_label = tk.Label(app, text="Client ID")
client_id_label.pack()

client_id_entry = tk.Entry(app)
client_id_entry.pack()

client_secret_label = tk.Label(app, text="Client Secret:")
client_secret_label.pack()

client_secret_entry = tk.Entry(app)
client_secret_entry.pack()

user_profile_url_label = tk.Label(app, text="User Playlist URL: ")
user_profile_url_label.pack()

user_profile_url_entry = tk.Entry(app)
user_profile_url_entry.pack()

#new section allows users to decide between outputting to csv or txt - this is just tkinter config stuff
output_options = ['csv', 'txt']
selected_option = tk.StringVar(app)
selected_option.set(output_options[0])

#creating the actual tkinter widgets for the new section (both the label and dropdown menu)
dropdown_label = tk.Label(app, text="Output to CSV or txt:")
dropdown_label.pack()

dropdown_menu = tk.OptionMenu(app, selected_option, *output_options)
dropdown_menu.pack()


start_button = tk.Button(app, text="Start", command=lambda: runProgram(user_profile_url_entry.get()))
start_button.pack()

def SpotiPySetup():
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id_entry.get(), client_secret=client_secret_entry.get())
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    return sp

def get_playlist_tracks(playlist_url, sp):
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

def runProgram(user_url):
    playlist_dictionary = userplaylists.scrape_spotify_playlists(user_url)
    for playlist_name, playlist_url in playlist_dictionary.items():
        song_list = get_playlist_tracks(playlist_url, SpotiPySetup())

        if (selected_option.get() == 'txt'):
            output.write_playlist_name_to_file(playlist_name)
            output.output_to_file(song_list)

        else:
            output.write_to_csv(song_list)


if __name__ == '__main__':
    app.mainloop()
    
