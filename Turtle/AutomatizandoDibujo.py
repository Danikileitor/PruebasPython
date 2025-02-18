import turtle

s = turtle.Screen()
t = turtle.Turtle()

'''t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)'''

'''for i in range(4):
    t.fd(100)
    t.rt(90)'''

resultado = input ("¿Quieres imprimir una figura?")
if resultado == "si":
    i = 0
    while i <= 100:
        t.circle(i)
        i += 10
else:
    print("Oka")

turtle.done()