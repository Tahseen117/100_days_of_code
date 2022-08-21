from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue", "green")

angles = [120, 90, 72, 60,40, 30]

for angle in angles:
    timmy.pencolor()
    for j in range(0,int(360/angle)):
        timmy.forward(100)
        timmy.right(angle)



screen = Screen()
screen.exitonclick()