# SpotiBackup
Backup a tracklist of all of your songs in your Spotify playlists!

This project utilizes SpotiPy and BeautifulSoup4 to compile a list of all of your public spotify playlists, and then outputs a tracklist text file containing every song. This is useful for those with large Spotify libraries who may fear a risk of losing access to these songs at any given time.

**USAGE**

Steps:
1. Head over to https://developer.spotify.com and create a developer account (and create a new app in the dashboard).
2. From the settings of your new developer app, find and store your CLIENT_ID and CLIENT_SECRET.
4. From there, just run main.py or run the SpotiBackup.exe from the releases page, and paste in your playlist link: (ex: https://open.spotify.com/user/YOUR_USERNAME_HERE/playlists) alongside your CLIENT_ID and CLIENT_SECRET


**WARNING: Please do not overuse the Spotify API. Repeated usages of this script (especially if you have a large library) will result in API timeouts and decreased functionality.**
