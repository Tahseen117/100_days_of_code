from tkinter import CENTER
from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,250)
        self.update_score()
        self.performer()

    def update_score(self):
        self.write(f"Score : {self.score}", align=CENTER, font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", font=('Arial', 30, 'normal'), align=CENTER)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.goto(0,250)
        self.update_score()
        self.performer()
    
    def highest_score(self, user_name):
        with open ('highest_score.txt', 'r+') as f:
            score1 = f.readline().split()
            if len(score1) > 0:
                if self.score > int(score1[-1]):
                    f.seek(0)
                    f.truncate()
                    f.write(f"Highest scorer : {user_name} : {self.score}")
                else:
                    pass
            else:
                f.write(f"Highest scorer : {user_name} : {self.score}")
    
    def performer(self):
        with open ('highest_score.txt', 'w+') as f:
            perf = f.read()
            self.goto(200,280)
        self.write(perf, font=('Arial', 10, 'normal'), align=CENTER)
