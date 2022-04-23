# # start to python day-19 code
# # starting code is basics learned
# # main project code at end
#
# # Author: Rushikesh Dikey
# # Date: 21-04-2022
#
#
# from turtle import Turtle, Screen
#
#
# # calling class
# tom = Turtle()
#
#
# def move_forward():
#     tom.forward(10)
#
#
# def move_backward():
#     tom.backward(10)
#
#
# def move_left():
#     new_heading = tom.heading() + 10
#     tom.setheading(new_heading)
#
#
# def move_right():
#     new_heading = tom.heading() - 10
#     tom.setheading(new_heading)
#
#
# def clear():
#     tom.clear()
#
#
# screen = Screen()
# screen.listen()
# screen.onkey(move_forward, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear, "c")
# screen.exitonclick()
#
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=1366, height=786)
screen.bgcolor("pink")
player_one = screen.textinput(title="PLAYER_ONE", prompt="Which turtle will win the race? Enter a color: ")
player_two = screen.textinput(title="PLAYER_TWO", prompt="Which turtle will win the race? Enter a color: ")
player_three = screen.textinput(title="PLAYER_THREE", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-200, -100, 0, 100, 200, 300]
all_turtles = []

# Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.shapesize(2)
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-650, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if player_one:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        # 230 is 250 - half the width of the turtle.
        if turtle.xcor() > 650:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == player_one or winning_color == player_two or winning_color == player_three:
                print(f"You've won! The {winning_color} turtle is the winner!")
                screen.textinput(title="Results!", prompt=f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                screen.textinput(title="Results!", prompt=f"You've lost! The {winning_color} turtle is the winner!")

        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()