import turtle
import time
import random

retraso = 0.1
puntos = int(0)
puntos_max = int(0)
ancho = int(1024)
alto = int(720)
bordeX = int(ancho / 2)
bordeY = int(alto / 2)

s = turtle.Screen()
s.setup(ancho, alto)
s.title("Snake")
s.bgcolor("whitesmoke")

bordeUp = turtle.Turtle("square", 1000, False)
bordeUp.penup()
bordeUp.pencolor("black")
bordeUp.speed(0)
bordeUp.goto(-bordeX + 10, bordeY - 10)
bordeUp.pendown()
bordeUp.fd(ancho - 20)

bordeDown = turtle.Turtle("square", 1000, False)
bordeDown.penup()
bordeDown.pencolor("black")
bordeDown.speed(0)
bordeDown.goto(-bordeX + 10, -bordeY + 10)
bordeDown.pendown()
bordeDown.fd(ancho - 20)

bordeRight = turtle.Turtle("square", 1000, False)
bordeRight.penup()
bordeRight.pencolor("black")
bordeRight.speed(0)
bordeRight.goto(bordeX - 10, -bordeY + 10)
bordeRight.pendown()
bordeRight.lt(90)
bordeRight.fd(alto - 20)

bordeLeft = turtle.Turtle("square", 1000, False)
bordeLeft.penup()
bordeLeft.pencolor("black")
bordeLeft.speed(0)
bordeLeft.goto(-bordeX + 10, -bordeY + 10)
bordeLeft.pendown()
bordeLeft.lt(90)
bordeLeft.fd(alto - 20)

snake = turtle.Turtle("square")
snake.speed(1)
snake.color("green")
snake.penup()
snake.home()
snake.viva = True
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
    global puntos
    global puntos_max
    cuerpo.append(c)
    puntos += 1
    if puntos > puntos_max:
        puntos_max = puntos


def actualizarCuerpo():
    longitud = len(cuerpo)
    for i in range(longitud - 1, 0, -1):
        cuerpo[i].goto(cuerpo[i - 1].xcor(), cuerpo[i - 1].ycor())
        cuerpo[i].showturtle()
    if longitud > 0:
        cuerpo[0].goto(snake.xcor(), snake.ycor())
        cuerpo[0].showturtle()


def muerte():
    snake.viva = False
    snake.direction = "stop"
    for i in cuerpo:
        i.clear()
        i.hideturtle()
    cuerpo.clear()


def arriba():
    if snake.viva:
        snake.direction = "up"


def abajo():
    if snake.viva:
        snake.direction = "down"


def derecha():
    if snake.viva:
        snake.direction = "right"


def izquierda():
    if snake.viva:
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

    if snake.ycor() > bordeUp.ycor():
        snake.speed(0)
        snake.goto(snake.xcor(), bordeDown.ycor())
        snake.speed(1)

    if snake.ycor() < bordeDown.ycor():
        snake.speed(0)
        snake.goto(snake.xcor(), bordeUp.ycor())
        snake.speed(1)

    if snake.xcor() > bordeRight.xcor():
        snake.speed(0)
        snake.goto(bordeLeft.xcor(), snake.ycor())
        snake.speed(1)

    if snake.xcor() < bordeLeft.xcor():
        snake.speed(0)
        snake.goto(bordeRight.xcor(), snake.ycor())
        snake.speed(1)

    if snake.distance(comida) < 20:
        generarComida()
        crecer()

    actualizarCuerpo()
    movimiento()

    for i in cuerpo:
        if i.distance(snake) < 20:
            muerte()

    time.sleep(retraso)

turtle.done()
