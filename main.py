import turtle

arrow = turtle.Turtle()
screen = turtle.Screen()
arrow.pencolor("red")
turtle.bgcolor("black")
arrow.speed(11)
arrow.penup()
arrow.goto(0, 150)
arrow.pendown()

F = 0
R = 0

while True:
    arrow.forward(F)
    arrow.right(R)

    F += 2
    R += 1
    if F == 380:
        break
    arrow.hideturtle()

turtle.done()
