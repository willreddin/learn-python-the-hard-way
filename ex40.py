class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_for_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you", "I don't want to get sued", "So I'll stop right there"])

bulls_on_parade = Song(["They rally round the family", "With a pocket full of shells"])

ripped_jeans = ["keep me in your pocket", "something about the rest", "Ever get pacier?"]


happy_bday.sing_for_me_a_song()

bulls_on_parade.sing_for_me_a_song()

foo = Song(ripped_jeans)

foo.sing_for_me_a_song()