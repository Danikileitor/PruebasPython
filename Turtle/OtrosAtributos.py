import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()'''

'''t.shape("arrow")
t.shape("circle")
t.shape("square")
t.shape("triangle")
t.shape("classic")'''
t.shape("turtle")

t.fd(100)
t.penup()
t.fd(50)
t.pendown()
t.fd(100)
t.undo()
t.clear()
t.reset()

t.fd(100)
t.stamp()
t.fd(100)

turtle.done()