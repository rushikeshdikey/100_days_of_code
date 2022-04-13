# start to python day-18 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 13-03-2022

############Turtle module#####################

# keyword module_name keyword thing_in_module

from turtle import Turtle, Screen, colormode
import random

# we can also write * to import all the classes
# from turtle import *

# aliases
# import turtle as t

# calling class
tom = Turtle()
# dick = Turtle()
# harry = Turtle()
# sam = Turtle()


# # changing the shape
# tom.shape("turtle")

# # changing the colour
# tom.color("orange")

# TODO: making our turtle move forward and move in square shape with and without loop
# tom.forward(100)
# tom.right(90)
# tom.forward(100)
# tom.right(90)
# tom.forward(100)
# tom.right(90)
# tom.forward(100)

# for _ in range(4):
#     tom.forward(100)
#     tom.left(90)

# for _ in range(4):
#     harry.backward(100)
#     harry.left(90)

# for _ in range(4):
#     dick.backward(100)
#     dick.right(90)

# for _ in range(4):
#     sam.forward(100)
#     sam.right(90)

# TODO: dashed line
# for _ in range(15):
#     tom.forward(10)
#     tom.penup()
#     tom.forward(10)
#     tom.pendown()

# TODO: drawing the shapes

# colours = ["navy", "red", "orange", "yellow", "blue", "pink", "purple", "green"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tom.forward(100)
#         tom.right(angle)

# for shape_side_n in range(3, 11):
#     tom.color(random.choice(colours))
#     draw_shape(shape_side_n)

# without using function
# for _ in range(4):
#     tom.forward(100)
#     tom.right(90)
# for _ in range(5):
#     tom.forward(100)
#     tom.right(72)
# for _ in range(6):
#     tom.forward(100)
#     tom.right(60)
# for _ in range(7):
#     tom.forward(100)
#     tom.right(51.42)
# for _ in range(8):
#     tom.forward(100)
#     tom.right(45)
# for _ in range(9):
#     tom.forward(100)
#     tom.right(40)
# for _ in range(10):
#     tom.forward(100)
#     tom.right(36)

# TODO: random walk
# TODO: create random colour

colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colour = (r, g, b)
    return random_colour

# colours = ["navy", "red", "orange", "yellow", "blue", "pink", "purple", "green"]
# direction = [0, 90, 180, 360]
# tom.pensize(10)
# tom.speed(3)
#
# for _ in range(200):
#     tom.color(random_colour())
#     tom.forward(30)
#     tom.setheading(random.choice(direction))

# TODO: spirograph

tom.speed("fastest")

# def draw_spirograph(size_of_gap):
#     for circle in range(int(360 / size_of_gap)):
#         tom.color(random_colour())
#         tom.circle(100)
#         tom.setheading(tom.heading() + size_of_gap)
#

# draw_spirograph(8)
#
# TODO: project dotted

tom.hideturtle()
tom.penup()


def draw_circle_with_color():
    for _ in range(10):
        tom.dot(15, random_colour())
        tom.forward(50)
        tom.setheading(90)
        tom.forward(50)
        tom.setheading(180)
        tom.forward(500)
        tom.setheading(0)


for _ in range(10):
    draw_circle_with_color()

screen = Screen()
screen.exitonclick()


