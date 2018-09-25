songs_count = int(input())
songs = []
for i in range(songs_count):
    songs_item = int(input())
    songs.append(songs_item)
print(songs)
for i in range(songs_count):
    if songs[i] == 10:
        songs[i] = 50
print(songs)
