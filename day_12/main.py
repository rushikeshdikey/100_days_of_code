# start to python day-12 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 02-03-2022

import random
import os
from time import sleep
# The screen clear function
def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')
screen_clear()

############Scope#############

# Local scope

# def runs_scored():
#    runs = 15
#    print(f"Inside fun{runs}")
#
# runs_scored()
# #print(f"Outside fun{runs}")
#
# # Global scope
#
# runs = 10
#
# def runs_scored():
#    runs_total = 15
#    print(f"Inside fun{runs}")
#
# runs_scored()
# print(f"Outside fun{runs}")
#
# # Global constant
# PI = 3.14159
#
# def pie():
#    print(PI)
#
# pie()
import random

# setting global variables
turn = 0
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def dificulty():
   '''function to check difficulty'''
   level = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()
   if level == 'easy':
      return EASY_LEVEL_TURN
   elif level == 'hard':
      return HARD_LEVEL_TURN
   else:
      return "Invalid difficulty level"

# function to compare the guess
def compare_number(answer, guess, turn):
   """checks answer against guess. Returns the number of turns remaining."""
   if answer > guess:
      print("Too Low")
      return turn - 1
   elif answer < guess:
      print("Too High")
      return turn - 1
   else:
      print(f"You guess it right, correct number is {answer}")

def game():
   print("Welcome to the Number Guessing Game!")
   print("I am thinking of a number between 1 to 100.")

   # to chosse random number to answer
   answer = random.randint(1, 100)

   # storing number of turn form function
   turn = dificulty()

   guess = 0
   while guess != answer:
      print(f"You have {turn} attempts remaining to guess the number.")
      guess = int(input("Make a guess:"))

      #Track the number of turns and reduce by 1 if they get it wrong.
      turn = compare_number(answer, guess, turn)
      if turn == 0:
         print("You are out of guess!!")
         return
      else:
         guess !=answer
         print("Guess again")

game()
