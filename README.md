# SpotiBackup
Backup a tracklist of all of your songs in your Spotify playlists!

This project utilizes SpotiPy and BeautifulSoup4 to compile a list of all of your public spotify playlists, and then outputs a tracklist text file containing every song. This is useful for those with large Spotify libraries who may fear a risk of losing access to these songs at any given time.

**USAGE**

**To use this script (in it's current state, this will be changed soon), you will need to edit the script slightly.
**

Steps:
1. Head over to https://developer.spotify.com and create a developer account (and create a new app in the dashboard).
2. From the settings of your new developer app, find and store your CLIENT_ID and CLIENT_SECRET.
3. In main.py, find the CLIENT_ID and CLIENT_SECRET variables and input your information.
4. From there, just run main.py, and paste in your playlist link: (ex: https://open.spotify.com/user/YOUR_USERNAME_HERE/playlists)

