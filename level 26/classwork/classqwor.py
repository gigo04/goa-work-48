from turtle import * 


def walk():
    forward(200)


def fall_back():
    right(180)
    forward(200)


def go_and_back():
    walk()
    fall_back()

go_and_back()
exitonclick()
