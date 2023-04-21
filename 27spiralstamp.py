import turtle as t
t.speed(5)
t.shape('triangle')
for i in range(40,-1,-1):
    t.stamp()
    t.forward(30)
    t.left(i)
t.done()