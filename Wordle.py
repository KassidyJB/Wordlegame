print('\033[46m'+'Hello!'+'\033[45m')

'''Wordle Game plan

1. Display alphabet
2. Display message that requests user to create a five letter word
3. (OPTIONAL) declare rules of the game/what messages to expect
4. Having the computer generate five letter words
5. Once the user inputs guess, use recursion to validate input before checking
for accuracy
6. Display user's tries/attempts, making sure to update them
7. While the game is going, check the player's word and letter
placement accuracy to keep the game flow.
8. If the player has the correct 5 letter word with all letters
in their correct places, display a message, stating they won'''

#Wordle Clone Outline
#Follow comments to help build out your game

#Set Up Game Variables. We will need variables to:
#store the number of guesses the player has made
#store the different colors we want to use
#keep track of letters that were guessed in the correct position
#letters guessed that were in the incorrect position 
#letters guessed that were not in the word at all.

tries = 0
Blue = '\033[34m'
Red = '\033[91m'
Green = ''
correct_pos = []
incorrect_pos = []
no_list = []



print(Red + '\033[0m')


#Create your Welcome message that explains how the game works

name = 



#Generate Word Function. Opens a word list file, then chooses a word at random

def generate_word():
  wordList = open("words.txt").read().split()
  word = random.choice(wordList)
  print('Word = ' + '_'*len(word))
  return word



#Get User Guess Function. Prompts user for a guess, checks to make sure it is a 5 letter word

def user():
    guess = input(f"Enter a five letter word.")



#Compare Words Function. 
# Compares the word guessed by the player to the solution word generated at random earlier.
#  Needs to check if each letter of the guess is in the solution word, and if so, 
# if it is in the correct position or not. Then it will print out the guess word again,
#  with each letter colored to reflect whether it was wrong, correct letter but
#  wrong position, or completely correct.





#Print Letters Function - Prints the entire alphabet for the user,
#  coloring all letters that have been guessed so far to reflect if those letters were
#  1. Not in the word at all
# 2. In the word but wrong position or 
# 3. In the word and correct position

def print_word(word, correct):
  progress = ''
  for let in word:
    if let in correct:
      progress += let
    else:
      progress += "_"
  return progress






#Game Loop. Calls the functions. Checks for win or lose conditions. Wins if all letters are in the correct place and there are less than 5 guesses.