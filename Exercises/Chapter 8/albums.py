#Excercise 8-7

def albuminfo(album_name, artist, songs=None):
    album = {
        'album_name' : album_name.title(),
        'artsit' : artist.title(),
    }

    if songs:
        album['songs'] = songs
    return album

encore = albuminfo('encore', 'eminem')
views = albuminfo('views', 'drake', 22)
stoney = albuminfo(songs=30, album_name='stoney', artist='pOst Malone')

print(encore)
print(views)
print(stoney)