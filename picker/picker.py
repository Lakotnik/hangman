import random
from nltk.corpus import words # Import collection of english words

wordlist = words.words()
class Picker:

	def __init__():
		self.words = words.words() # retrieve all the words from nltk
		self.
		####
		# If at some point I decide to make settings readable from a file
		# this is where they should be read in
		###

	def random_word():
		while True:
			rand_word = random.choice(self.words)
			if len(rand_word) > 4: # make sure we don't get anything too short
				return rand_word

	def mainLoop(start):
		# Things that need their own methods
		# 1. get random word from word list
		# 2. Initialize the player field. Number of letters, all that jazz
		# 3. Wait for player input
		# 4. On player input print new state of the game
		current_word = None
		current_gamestate = None
		while True:
			if not current_gamestate:
				if not current_word:
					if start:
						current_word = random_word()
					else:
						choice = input("Start new game? (y/n) ")
						if choice in ['Y','y']:
							current_word = random_word()
						elif choice in ['N','n']:
							exit()
						else:
							continue
				else:
					current_word = None # if we don't have a gamestate but a word is somehow still here, clear it
					continue
			else:
				# we have a gamestate and hopefully a word, lets check for that first
				if not current_word:
					# then we're in a bit of trouble
					current_gamestate = None # reset gamestate because we have no word and start over
					continue
				else:
					# here we can do actual game logic then. Not just checking that everything is alright
					



