from asyncio.proactor_events import _ProactorBasePipeTransport
from turtle import Turtle, Screen
import time


STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT =0 

class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]
        self.head.color('white')

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
               
    def add_segment(self, position):
        turtle = Turtle(shape='square')
        turtle.penup()
        turtle.color('orange')
        turtle.goto(position)
        self.segment.append(turtle)

    def extend(self):
        self.add_segment(self.segment[-1].position())
    
    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x,new_y)
        self.segment[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)
    
    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)
    
    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)
    
    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)
