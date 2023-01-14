song = input()
new_song = song.split('WUB')
first_word = next(s for s in new_song if s)
idx_fw = new_song.index(first_word)
new_song = new_song[idx_fw:]
new_song = ' '.join(new_song)
print(new_song)