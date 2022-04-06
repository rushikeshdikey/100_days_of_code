# start to python day-7 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 12-03-2022

import random
import os
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# creating word list
word = ['Rushi', 'Arpit', 'Gunjan', 'Ankit']
random_word = random.choice(word).lower()
word_length = len(random_word)

# count of lives
lives = 6

# to check the word
# print(random_word)

# create blanks
display = []
for _ in range(word_length):
    display +="_"

end_of_game = False
# while loop
while not end_of_game:
    # guess the word
    guess = input("Guess the letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}")
# for checking the guess in word
    for position in range(word_length):
        letter = random_word[position]
        if letter == guess:
            display[position] = letter

    # If guess is not a letter in the chosen_word
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."

    if guess not in random_word:
        print(f" You guessed {guess}, that's not in word, you lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    print(stages[lives])
