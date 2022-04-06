# start to python day-4 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 08-03-2022

# random number
import random

# random_integer = random.randint(0, 1)
# print(random_integer)
#
# random_float = random.random()
# print(random_float)
#
# print(round(random_float * 5, 2))
#
# flip a coin

# print("FLip a Coin")
#
# side = input("Type toss to flip the coin ").lower()
#
# if side == 'toss':
#     flip = random.randint(0, 1)
#     if flip == 1:
#         print("Heads")
#     else:
#         print("Tails")
# else:
#     print("Please type toss to flip a coin")

# Who will pay the bill generator

# names = input("Please enter the names seperated by commas ")
#
# split_names = names.split(", ")

# print(split_names)
#
# len_names = (len(split_names))
# payee = random.randint(1, len_names - 1)
# print(f"{split_names[payee]} is going to pay the bills")

# directly above code in 2 lines
# payee = random.choice(split_names)
#
# print(payee)

#fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
#
# dirty_dozen = [fruits, vegetables]
#
# print(dirty_dozen[1][1])

# Rock Paper Scissors
print("Welcome to ROCK PAPER & SCISSOR")
user = int(input("Choose from your choice? 0 for Rock, 1 for Paper, 2 Scissor\n"))

rock = 'ROCK'
paper = 'PAPER'
scissors = "SCISSOR"

user_choice = [rock, paper, scissors]
computer = random.randint(0, 2)
#print(f"Computer_choice \n{user_choice[computer]}")
if user >= 3 or user < 0:
    print("Invalid input, you lose")
else:
    print(f"User_choice \n{user_choice[user]}")

print(f"Computer_choice \n{user_choice[computer]}")

if user >= 3 or user < 0:
    print("Invalid input, you lose!")
elif user == 0 and computer == 2:
    print("You WON!")
elif user == 2 and computer == 0:
    print("You LOSE!")
elif user == computer:
    print("Its Draw")
elif user > computer:
    print("You WON!")
elif computer > user:
    print("You LOSE!")