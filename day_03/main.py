# start to python day-3 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 07-03-2022

# Leap year calculator

# year = int(input("Enter year to check is it a leap year or not "))
#
# if(year%4 == 0):
#     if(year%100 == 0):
#         if(year%400 == 0):
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")
#
# Rollercoaster entry

# print("Welcome to the Rollercoaster\n")
#
# hieght = int(input("What is your hieght in cms? "))
# bill = 0
#
# if hieght >= 120:
#     print("You can ride the rollercoster")
#     age = int(input("Enter your age: "))
#
#     if age < 12:
#         print("Child tickets are ₹5")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are ₹7")
#         bill = 7
#     else:
#         print("Adult tickets are ₹12")
#         bill = 12
#     photo = input("Do you want photograph? enter Y or N: ")
#
#     if photo == 'Y':
#         bill = bill +3
#         print(f"Total bill is ₹ {bill}")
#     else:
#         print(f"Total bill is ₹ {bill}")
#
# else:
#     print("Sorry, you can grow your taller before you ride")

# Pizza bill generator

# print("Welcome to DK's Pizza")
#
# size = input("What size pizza do you want S, M or L: ")
# pepperoni = input("Do you want pepperoni Y or N: ")
# chesse = input("Do you want extra chesse Y or N: ")
#
# bill = 0
#
# if size == 'S':
#     bill = 250
# elif size == 'M':
#     bill  = 550
# else:
#     bill = 850
#
# if pepperoni == 'Y':
#     if size == 'S':
#         bill += 50
#     elif size == 'M':
#         bill += 80
#     elif size == 'L':
#         bill +=110
# if chesse == 'Y':
#         bill += 30
# else:
#     print("Try adding cheese")
#
# print(f"Your final bill is: ${bill}.")

# Love calculator

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
#
# combined_name = name1 + name2
# lower_case = combined_name.lower()
#
# t = lower_case.count("t")
# r = lower_case.count("r")
# u = lower_case.count("u")
# e = lower_case.count("e")
#
# true = t + r + u + e
#
# l = lower_case.count("l")
# o = lower_case.count("o")
# v = lower_case.count("v")
# e = lower_case.count("e")
#
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
# print (love_score)
#
# if (love_score < 10) or (love_score > 90):
#     print(f"Your love score is {love_score}, you go together")
# elif (love_score >=40) and (love_score <=50):
#     print(f"Your love score is {love_score}, you are alright together")
# else:
#     print("leave it")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()

if choice1 == 'right':
    print("It\'s a room full of fire. Game Over.")
elif choice1 == 'left':
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
    if choice2 == 'swim':
        print("You fell into a hole. Game Over.")
    elif choice2 == 'wait':
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()
        if choice3 == 'red' or choice3 == 'blue':
            print("You chose a door that doesn't exist. Game Over.")
        else:
            print("You found the treasure! You Win!")