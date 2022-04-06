# start to python day-1 code
# starting code is basics_learnt
# main project code at end

# Author: Rushikesh Dikey
# Date: 03-03-2022

'''
# printing by taking input from user

print("You Band_Name is: " + input("Enter your Name:") + " " + input("Enter your Surname:"))

# Length calculator

username = input("Enter your Band_name:")
length = len(username)
print(length)

# interchanging variables

a = input("a:")
b = input("b:")

temp = a
a = b
b = temp

print("a = " + a)
print("b = " + b)

'''

#Band Name Generator
print("Welcome to Band Name Generator")
print("Enter few details to generate your Band_Name")

city_name = input("Enter the city that you grow up in:\n")
pet_name = input("Enter your pet name:\n")

print("Your Band_Name is: " + city_name + "-" + pet_name)