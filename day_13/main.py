# start to python day-13 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 05-03-2022

############DEBUGGING#####################

# Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20: # erorr here as i value is out of the range
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # error here as integer are denoting out of the index value (0, 5) will work
# print(dice_num)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")
# else:
#     print(f"You are not allowed to drive at {age}")

# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# #print(pages)
# word_per_page = int(input("Number of words per page: "))
# #print(word_per_page)
#
# total_words = pages * word_per_page
# print(total_words)

# Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)
#
# mutate([1,2,3,5,8,13])

# matrix= []
# R = int(input("Number of rows: "))
# C = int(input("Number of columns: "))
# for i in range(R):
#     a = []
#     for j in range(C):
#         a.append(int(input("Enter: ")))
#     matrix.append(a)
#
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end= " ")
#     print()


# number = int(input("Which number do you want to check?"))
#
# if number % 2 == 0:
#     print("This is an even number.")
# else:
#     print("This is an odd number.")

