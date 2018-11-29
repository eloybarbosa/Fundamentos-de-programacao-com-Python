#7. Utilizando a ferramenta turtle, desenhe uma série de quadrados um do lado do outro como indicada na figura a seguir:

import turtle

turtle.penup()
turtle.left(180)
turtle.forward(200)
turtle.left(180)
turtle.pendown()

for c in range (100, 500, 100):
    for count in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.forward(100)
turtle.done()





