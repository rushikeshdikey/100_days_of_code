# start to python day-5 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 09-03-2022

# fruits = ["Apple", "Oranges", "Grapes"]
# for fruit in fruits:
#     print(fruits)
#     print(fruit + " Pie")
# print(fruit)

# print("Welcome to average height calculator")
# height = input("Enter the height of students ").split()
# for n in range(0, len(height)):
#     height[n] = int(height[n])
# #print(height)
#
# add = 0
# for h in height:
#     add += h
# #print(add)
# average = round(add / len(height))
#
# print(f"The average height of students is {average}")

# Highest number
# scores = input("Enter the scores of the student ").split()
#
# for n in range(0, len(scores)):
#     scores[n] = int(scores[n])
# print(scores)
# # logic 1
# high = 0
# for score in scores:
#     if score > high:
#         high = score
# print(f"The highest score in the class is: {high}")
# #logic 2
# scores.sort()
# print(f"The highest score in the class is: {scores[-1]}")

#for loop with range
# i = int(input("From: "))
# j = int(input("To: "))
# total = 0
# for number in range(i, j+1):
#     total += number
# print(total)

#adding even numbers
##logic 1
# total = 0
# for number in range(1, 101, 2):
#     #print(number)
#     total += number
# print(total)
# #logic 2
# total1 = 0
# for number in range(1, 101):
#     #print(number)
#     if number % 2 == 0:
#         total1 += number
# print(total)

#FUZZBIZZ
for i in range(1, 101):
    #divisble by both 3 and 5
    if i % 3 == 0 and i % 5 == 0:
        i = 'FizzBuzz'
    # divisble by 3
    elif i % 3 == 0:
        i = 'Fizz'
    # divisble by 5
    elif i % 5 == 0:
        i = 'Buzz'
    print(i)