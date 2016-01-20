import time

interlude_1 = ["Don't let me drown, don't breath alone.",
	  "No kicks, no pangs, no broken bones.",
	  "Never let me sink, always feel at home.",
	  "No sticks, no shanks and no stones.",
	  "Never leave it too late, always enjoy the taste,",
	  "Of the great grey world of hearts."]

def print_lyrics(input, tempo):
	"""Prints the values of the array of lyrics
	Args:
		input: Array containing the lyrics.
		tempo: Speed of diction in sec.
	"""
	for element in input:
		print element	
		time.sleep(tempo)

if __name__ == '__main__':
	print_lyrics(interlude_1, 4)
	
