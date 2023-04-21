import turtle
import random
t=turtle.Turtle()
t.speed(0)
t.width(5)
colors=["red","blue","green","yellow","black"]
def penup():
    t.penup()
def pendown():
    t.pendown()
def up():
    t.setheading(90)
    t.forward(50)
def down():
    t.setheading(270)
    t.forward(50)
def right():
    t.setheading(0)
    t.forward(50)
def left():
    t.setheading(180)
    t.forward(50)
def leftclick(x,y):
    t.color(random.choice(colors))
def rightclick(x,y):
    t.stamp()
turtle.listen()
turtle.onscreenclick(leftclick,1)
turtle.onscreenclick(rightclick,3)
turtle.listen()
turtle.onkey(up,"Up")
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")
turtle.onscreenclick(leftclick,1)
turtle.onscreenclick(rightclick,2)
turtle.onkey(penup,"<")
turtle.onkey(pendown,">")
turtle.done()