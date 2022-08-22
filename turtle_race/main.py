import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800,height=500)
user_bet= screen.textinput(title="Make your bet", prompt="Who will win the race. Enter your colour :")
print(user_bet)

color = ['red', 'blue', 'green', 'orange', 'purple']
y_coordinate = [200, 100, 0, -100, -200]
turtles = []

for turtle in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle])
    #new_turtle.speed("fastest")
    new_turtle.goto(-390,y_coordinate[turtle])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() > 370:
            is_race_on = False
            winner = t.pencolor()
            if winner == user_bet:
                print(f'You have won ! {winner} is the winner !!')
            else:
                print(f'You Lost :(, {winner} is the winner !!')
        t.forward(random.randint(0,10))


screen.exitonclick()
