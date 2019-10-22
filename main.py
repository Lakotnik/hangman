#!/usr/bin/env python3
# import solver
# import picker

non_func = " [[Not yet functional]]"

def printWelcome():
	print("Welcome to hangman! Please select your gamemode.")
	print("[1] Try to guess a word." + non_func)
	print("[2] The bot tries to guess your word." + non_func)

# returns input if good, prints error and exits if not
def validateInput(user_input):
	for i in range(1,2):
		if user_input == str(i):
			
	# if type(user_input) == int:
	# 	if user_input <= 2 and user_input > 0:
	# 		print("You have selected option {}.".format(user_input))
	# 		return user_input
	# 	else:
	# 		print("Option is out of range!")
	# 		exit()
	# else:
	# 	print("Option is not a number!")
	# 	exit()

def gameStart():
	printWelcome()
	user_input = input()
	user_input = validateInput(user_input)
	if user_input == 1:
		# picker.mainLoop()
		pass
	elif user_input == 2:
		# solver.mainLoop()
		pass


if __name__ == '__main__':
	gameStart()