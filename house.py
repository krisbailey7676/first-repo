# Turtle Party Project - draw house
# by Kris Bailey 2/19/2024

from turtle import *

speed(1)
shape("turtle")


def square(len):
    for i in range(4):
        forward(len)
        right(90)


def triangle(len):
    for i in range(3):
        forward(len)
        left(120)


def house(clr, wdth, len):
    pendown()
    color(clr)
    width(wdth)
    square(len)
    triangle(len)
    penup()


def main():
    house("red", 3, 100)
    backward(150)
    house("purple", 5, 75)
    backward(100)
    house("blue", 4, 50)


main()

Screen().exitonclick()
