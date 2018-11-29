#6. Utilizando a ferramenta turtle, desenhe os ângulos de um círculo como indicado na figura a seguir:

import turtle

for c in range (0, 360, 15):
    turtle.shape('turtle')
    turtle.speed(10)    
    turtle.setheading(c)
    turtle.forward(150)
    turtle.backward(150)
turtle.done()

