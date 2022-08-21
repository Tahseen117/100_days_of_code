from random import random
from turtle import Turtle, Screen
import turtle as t
import random

timmy = Turtle()
t.colormode(255)
timmy.speed('fastest')

def pick_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size):
    for _ in range(int(360/size)):
        timmy.color(pick_colour())
        timmy.circle(100)
        timmy.forward(5)
        timmy.setheading(timmy.heading()+5)

draw_spirograph(5)
screen = Screen()
screen.exitonclick()