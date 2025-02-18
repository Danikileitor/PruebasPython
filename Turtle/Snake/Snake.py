import turtle
import time
import random

retraso = 0.1
puntos = 0
puntos_max = 0

s = turtle.Screen()
s.setup(1024, 720)
s.title("Snake")
s.bgcolor("whitesmoke")

snake = turtle.Turtle()
snake.speed(1)
snake.shape("square")
snake.color("green")
snake.penup()
snake.home()
snake.direction = "stop"


def movimiento(snake):
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


while True:
    s.update()
    movimiento(snake)
    time.sleep(retraso)

turtle.done()
