import turtle
import time
import random

retraso = 0.1
puntos = 0
puntos_max = 0
ancho = int(1024)
alto = int(720)
bordeX = int(ancho / 2)
bordeY = int(alto / 2)

s = turtle.Screen()
s.setup(ancho, alto)
s.title("Snake")
s.bgcolor("whitesmoke")

snake = turtle.Turtle("square")
snake.speed(1)
snake.color("green")
snake.penup()
snake.home()
snake.direction = "stop"

comida = turtle.Turtle("circle")
comida.color("orange")
comida.penup()
comida.speed(0)

cuerpo = []


def generarComida():
    comida.goto(
        random.randint(-bordeX + 50, bordeX - 50),
        random.randint(-bordeY + 50, bordeY - 50),
    )


def crecer():
    c = turtle.Turtle("square", 1000, False)
    c.color("green")
    c.penup()
    c.speed(0)
    cuerpo.append(c)


def actualizarCuerpo():
    longitud = len(cuerpo)
    for i in range(longitud - 1, 0, -1):
        cuerpo[i].goto(cuerpo[i - 1].xcor(), cuerpo[i - 1].ycor())
        cuerpo[i].showturtle()
    if longitud > 0:
        cuerpo[0].goto(snake.xcor(), snake.ycor())
        cuerpo[0].showturtle()


def arriba():
    snake.direction = "up"


def abajo():
    snake.direction = "down"


def derecha():
    snake.direction = "right"


def izquierda():
    snake.direction = "left"


def movimiento():
    match snake.direction:
        case "up":
            snake.sety(snake.ycor() + 20)
        case "down":
            snake.sety(snake.ycor() - 20)
        case "right":
            snake.setx(snake.xcor() + 20)
        case "left":
            snake.setx(snake.xcor() - 20)
        case _:
            pass


s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")
generarComida()

while True:
    s.update()

    if snake.distance(comida) < 20:
        generarComida()
        crecer()

    actualizarCuerpo()
    movimiento()
    time.sleep(retraso)

turtle.done()
