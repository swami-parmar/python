
from playlist import add_song, remove_song, display_playlist

playlist = []

# Add three songs
add_song("Kesariya", playlist)
add_song("Shape of You", playlist)
add_song("Believer", playlist)

print("Playlist after adding songs:")
display_playlist(playlist)

# Remove a song
remove_song("Shape of You", playlist)

print("\nPlaylist after removing a song:")
display_playlist(playlist)
