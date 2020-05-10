#Authors: Prince Rios and Edward Cluster
#Date: 19 February 2020
#Description: This code creates a class called Song and uses the __init__ constructer to initialize the different
#variables given. There is also a print_song method in the class to display the attributes of the song.
#Then, two objects of type Song are created and printed using print_song. 
class Song:
	def __init__(self, artist, genre, length, album, songName):
		self.artist = artist
		self.genre = genre
		self.length = length
		self.album = album
		self.songName = songName
	def print_song(self):
		print("Artist:", self.artist, "\n", "Genre:", self.genre, "\n", "Length:", self.length, "minutes long", "\n", "Album name:", self.album)
	def get_artist(self):
		return self.artist
	def get_songName(self):
		return self.songName
song1 = Song("Lil Baby", "Rap", 4, "Drip 2 Hard", "Freestyle")
song2 = Song("Michael Jackson", "Soft Rock", 5, "Thriller", "Wanna Be Startin Something")
song1.print_song()
song2.print_song()
print(song1.get_artist())
print(song1.get_songName())
print(song2.get_songName())
