"""
This game was written by Thor.N from scratch.
Started on the 16/4/2021 2:10
Second attempt after starting from scratch on 13/07/2021 00:12
"""


import os

clear = lambda: os.system('cls')

def pause():

	print(' ')
	input('Press enter to continue...')




hangManDiagram = {
	9: "",
	8: "____",
	7: "\n|\n|\n|\n|\n|\n|____",
	6: "______\n|\n|\n|\n|\n|\n|____",
	5: "______\n|    |\n|\n|\n|\n|\n|____",
	4: "______\n|    |\n|    O\n|\n|\n|\n|____",
	3: "______\n|    |\n|   _O_\n|\n|\n|\n|____",
	2: "______\n|    |\n|   _O_\n|    |\n|\n|\n|____",
    1: "______\n|    |\n|   _O_\n|    |\n|   /\n|\n|____",
	0: "______\n|    |\n|   _O_\n|    |\n|   / \ \n|\n|____"

}




def hangMan():
	clear()
	
	input_word = input("Please enter a word to guess (no spaces): ").lower()
	print(' ')
	pausemessaage = input("Press enter to clear the console...")
	clear()
	
	already_guessed = ''
	letters_to_guess = ''
	letters_left = len(input_word)
	lives_left = 9
	for i in input_word:
		letters_to_guess += '_'
	
	#loops until all letters have been guessed
	while (letters_left > 0) and (lives_left > 0):
		print(' ')
		print(' ')
		print(hangManDiagram[lives_left])
		print(' ')
		print(' ')

		print('You have ' + str(lives_left) + ' lives left.')
		print('letters to guess:', letters_to_guess)
		guessed_letter = input('Guess a letter: ')
		print(' ')


		if len(guessed_letter) == 1: #makes sure there is an input

			#checks if letter was already guessed
			if (guessed_letter not in already_guessed) and (guessed_letter in input_word): 

				for i in range(len(input_word)):
					if (input_word[i] == guessed_letter):

						#changes variables so that it is ready for next guess
						letters_to_guess = letters_to_guess[:i] + input_word[i] + letters_to_guess[i+1:]
						letters_left -= 1
						already_guessed += input_word[i]
						clear()
						print('CORRECT!')
						print(' ')

			#if the word has already been guessed:
			elif (guessed_letter in already_guessed):
				lives_left -= 1
				clear()
				print(' ')
				print('You already guessed "' + guessed_letter + '"')
				print('-1 life')
				print(' ')
			
			else:
				lives_left -= 1
				clear()
				print(' ')
				print('Sorry, "' + guessed_letter + '" is not in the word')
				print('-1 life')
				print(' ')

		else:
			print('Please enter 1 character to be guessed.')
			pause()
			clear()
			continue
	clear()

	#result of the game
	if letters_left == 0:
		print('CONGRADULATIONS, you guessed the word:', input_word)
		print(' ')
	elif lives_left == 0:

		print(' ')
		print(hangManDiagram[0])
		print('Sorry, you failed to guess the word.')
		print('The word was:', input_word)
		print(' ')

clear()

hangMan()
playAgain = True
#checks if player wants to play again
while playAgain:
	print('Would you like to play again?')
	choice = input('y for yes, n for no: ')
	if choice == 'n':
		hangMan()
	elif choice == 'n':
		playAgain = False
	else:
		clear()
        print('\nPlease enter a valid answer.')
        input('\nPress Enter to answer again...')

clear()