#05. Usando a biblioteca ‘turtle’ crie uma função que desenhe a imagem a seguir:

import turtle

tamanho = 600
margem = 40
X = -300
Y = -300


def quadrado(x, y):
    turtle.shape('turtle')
    turtle.speed(100)
    turtle.penup()
    turtle.setx(x + margem)
    turtle.sety(y + margem)

    turtle.pendown()
    turtle.setx(turtle.xcor() + tamanho - 2 * margem)
    turtle.sety(turtle.ycor() + tamanho - 2 * margem)

    turtle.setx(turtle.xcor() - tamanho + 2 * margem)
    turtle.sety(turtle.ycor() - tamanho + 2 * margem)


def circulo(x, y):
    turtle.shape('turtle')
    turtle.speed(100)
    turtle.penup()
    turtle.setx(x + margem + (tamanho - margem * 2) / 2)
    turtle.sety(y + margem)

    turtle.pendown()
    turtle.circle((tamanho - margem * 2) / 2)


quadrado(X, Y)

for i in range(8):

    tamanho = tamanho / 2 - margem
    X += margem
    Y += margem
    margem /= 2

    quadrado(X, Y)
    quadrado(X, Y + tamanho)
    circulo(X + tamanho, Y)
    circulo(X + tamanho, Y + tamanho)


turtle.done()
