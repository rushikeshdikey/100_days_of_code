# start to python day-6 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 10-03-2022

# def my_function():
#     print("Hello")
#
# my_function()
#
# def add(a, b):
#     print(a + b)
#
# def sub(a, b):
#     print(a - b)
#
# def mul(a, b):
#     print (a * b)
#
# def div(a, b):
#     print (a / b)
#
# a = int(input("first number:"))
# b = int(input("second number:"))
# c = input("type what you want to do: ").lower()
#
# if c == 'add':
#     add(a, b)
# elif c == 'sub':
#     sub(a, b)
# elif c == 'mul':
#     mul(a, b)
# elif c == 'div':
#     if b == 0:
#         print("Cannot divide by zero")
#     else:
#         div(a, b)
# else:
#     print("type correct function")

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json
print below code on above website for 'hurdle 4'
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()


while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
print below code on above website for 'maze'
def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
