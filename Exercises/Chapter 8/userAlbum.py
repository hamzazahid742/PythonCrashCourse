#Exercise 8-8

def albuminfo(album_name, artist, songs=None):
    album = {
        'album_name' : album_name.title(),
        'artsit' : artist.title(),
    }

    if songs:
        album['songs'] = songs
    return album

while True:
    print('\n Please enter the album info ')
    print('(Enter q to quit at anytime ')
    album_name = input('Enter the album name ')
    if album_name == 'q':
        break
    artist_name = input('Enter the artist name ')
    if artist_name == 'q':
        break
    songs = input('Enter the number of songs in the album ')
    if songs == 'q':
        break
    useralbum = albuminfo(album_name, artist_name, songs)
    print(useralbum)
