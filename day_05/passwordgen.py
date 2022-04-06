# start to python day-5 code
# Author: Rushikesh Dikey
# Date: 09-03-2022

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#random_letter = random.choice(letters)
#random_number = random.choice(numbers)
#random_symbols = random.choice(symbols)
password = []
for letter in range(1, nr_letters + 1):
    password.append(random.choice(letters))
for number in range(1, nr_numbers + 1):
    password.append(random.choice(numbers))
for symbol in range(1, nr_symbols + 1):
    password.append(random.choice(symbols))
#print(password)
random.shuffle(password)
#print(password)

final_password = ""
for char in password:
    final_password+= char
print(f"Your new password is: {final_password}")