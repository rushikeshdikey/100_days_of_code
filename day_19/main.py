# start to python day-19 code
# starting code is basics learned
# main project code at end

# Author: Rushikesh Dikey
# Date: 21-04-2022


from turtle import Turtle, Screen


# calling class
tom = Turtle()


def move_forward():
    tom.forward(10)


def move_backward():
    tom.backward(10)


def move_left():
    new_heading = tom.heading() + 10
    tom.setheading(new_heading)


def move_right():
    new_heading = tom.heading() - 10
    tom.setheading(new_heading)


def clear():
    tom.clear()


screen = Screen()
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()







