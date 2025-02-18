import turtle
import random

s = turtle.Screen()
s.setup(1024, 720)
s.title("Carrera de Tortugas")
s.bgcolor("whitesmoke")

j1 = turtle.Turtle()
j1.hideturtle()
j2 = turtle.Turtle()
j2.hideturtle()

j1.shape("turtle")
j1.color("green", "green")
j1.shapesize(2, 2, 2)
j1.pensize(3)

j2.shape("turtle")
j2.color("blue", "blue")
j2.shapesize(2, 2, 2)
j2.pensize(3)

j1.penup()
j1.goto(300, 200)
j1.pendown()
j1.circle(40)

j2.penup()
j2.goto(300, -200)
j2.pendown()
j2.circle(40)

j1.penup()
j1.goto(-300, 240)
j1.pendown()
j1.showturtle()

j2.penup()
j2.goto(-300, -160)
j2.pendown()
j2.showturtle()

turtle.done()
