import turtle
 
# defining colors
colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
 
# setup turtle pen
t= turtle.Pen()
 
# changes the speed of the turtle
t.speed(30)
 
# changes the background color
turtle.bgcolor("black")
 
# make spiral_web
for x in range(250):
    t.pencolor(colors[x%6]) # setting color
    t.width(x/100 + 1) # setting width
    t.forward(x+((x+1)/2)) # moving forward
    t.left(59) # moving left
t.left(50)
t.forward(75)
 
turtle.done()