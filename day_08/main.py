# start to python day-8 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 13-03-2022

import math
# def great():
#     print("My name is Rushikesh Dikey")
#     print("My age is 25")
#     print("I leave at Amravati")
#
#
# great()
#
#
# def greet_with_name(name, location):
#     print(f"My name is {name}")
#     print(f"How do you do {name}?")
#     print(f"I live in {location}")
#
#
# name = input("Enter your name: ")
# location = input("Enter your location: ")
#
# greet_with_name(name, location)
#

# Paint area Calculator
#
# wall_height = int(input("Enter height of the wall: "))
# wall_width = int(input("Enter width of the wall: "))
#
# coverage = 5
#
# # use ceil function to round up
# def paint_calc(wall_height, wall_width, coverage):
#     number_of_cans = math.ceil((wall_height * wall_width) / coverage)
#     print(f"Number of cans required: {number_of_cans}")
#
#
# paint_calc(wall_height, wall_width, coverage)


# def prime_checker(number):
#     is_prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             is_prime = False
#     if is_prime:
#         print("It is a prime number")
#     else:
#         print("Its is not prime")
#
#
# number = int(input("Enter the number: "))
# prime_checker(number)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(plain_text, shift_amount, direction):
    if direction == 'encode':
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The encrypt text is {cipher_text}")


def decrypt(plain_text, shift_amount, direction):
    if direction == 'decode':
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        print(f"The decrypt text is {cipher_text}")

decide = True
while decide:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    encrypt(text, shift, direction)
    decrypt(text, shift, direction)

    result = input("Do you want to continue: ")
    if result == "no":
        decide = False
        print("Goodbye")