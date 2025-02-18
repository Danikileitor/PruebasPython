import turtle
import random
import time

s = turtle.Screen()
s.setup(1024, 720)
s.title("Carrera de Tortugas")
s.bgcolor("whitesmoke")

j1 = turtle.Turtle()
j1.hideturtle()
j2 = turtle.Turtle()
j2.hideturtle()
radio = 50

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
j1.circle(radio)

j2.penup()
j2.goto(300, -200)
j2.pendown()
j2.circle(radio)

j1.penup()
j1.goto(-300, 200 + radio)
j1.showturtle()

j2.penup()
j2.goto(-300, -200 + radio)
j2.showturtle()

while j1.xcor() < 300 - radio and j2.xcor() < 300 - radio:
    time.sleep(1)
    j1.fd(10 * random.randrange(1, 6))
    j2.fd(10 * random.randrange(1, 6))

if j1.xcor() >= 300 - radio and j2.xcor() >= 300 - radio:
    print("Empate")
elif j1.xcor() >= 300 - radio:
    print("La tortuga verde ha ganado")
else:
    print("La tortuga azul ha ganado")

turtle.done()
