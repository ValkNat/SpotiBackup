#imports
import csv


def output_to_file(dataset):

    with open('output.txt', 'a', encoding='utf-8') as file:
        for line in dataset:
            file.write(f'{line}\n')


def output_dict_to_file(result):
    with open('playlists.txt', 'w') as file:
        for playlist_name, playlist_url in result.items():
            file.write(f'{playlist_name} - {playlist_url} \n')


def write_playlist_name_to_file(playlist_name):
    with open('output.txt', 'a', encoding='utf-8') as file:
        file.write(f'#### {playlist_name} ####')

def write_to_csv(song_list):
    with open('tracklist.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for song in song_list:
            writer.writerow([song])

    
