# start to python day-1 code
# starting code is basics
# main project code at end

# Author: Rushikesh Dikey
# Date: 04-03-2022

'''
num_char = len(input("What is your name: "))
con_str = str(num_char)
print("Your name has " + con_str + " characters")

type casting example
a = str(123)
print(type(a))

print and add digits

digit = input("Enter two numbers: ")
digit_one = digit[0]
#a = int(digit_one)
#print(type(a))

digit_second = digit[1]
#b = int(digit_second)
#print(type(b))

#add = a + b
add = int(digit_one) + int(digit_second)

print(add)


BMI Calculator

print("Welcome to BMI calculator")
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kgs: "))

# h = float(height)
# w = float(weight)

bmi = int(weight / height ** 2)

print("Your BMI is: " + str(bmi))

if bmi > 25:
    print("You are Obese")
elif bmi < 25 > 15:
    print("You are Ideal")
else:
    print("You are Underweight")
'''

# BMI Calculator
#
# print("Welcome to BMI calculator")
# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in Kgs: "))
#
# # h = float(height)
# # w = float(weight)
#
# bmi = round(weight / height ** 2)
#
# #print(f"Your BMI is: {bmi}")
#
# if bmi < 18.5:
#     print(f"Your BMI is: {bmi}, you are Under weight.")
# elif bmi < 25:
#     print(f"Your BMI is: {bmi}, you are Normal weight.")
# elif bmi < 30:
#     print(f"Your BMI is: {bmi}, you are Over weight.")
# else:
#     print(f"Your BMI is: {bmi}, are Obese")

# TIP calculator
print("Welcome to TIP calculator")
bill_amount = float(input("What was the total bill? ₹"))
percentage_of_tip = float(input("What percentage tip would you like to give? "))
members = int(input("How many people to split the bill? "))

split = bill_amount / members
payment = (bill_amount * percentage_of_tip) / 100
pay = round(payment / members, 2) + split

print(f"Each person should pay: ${pay}")
