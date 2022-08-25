from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.speed('slow')
    
    def move(self):
        new_x_cor = self.xcor() + 10
        new_y_cor = self.ycor() + 10
        self.goto(new_x_cor,new_y_cor)
