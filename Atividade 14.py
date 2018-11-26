import turtle
turtle.title("Desenhando Quadrado, Triângulo e Circulo utilizando 'Onkey' Teclas: cima, baixo, esquerda, direita, q, t ,c")

def cima():
    turtle.penup()
    turtle.setheading(90)
    turtle.forward(50)
    turtle.pendown()

def baixo():
    turtle.penup()
    turtle.setheading(270)
    turtle.forward(50)
    turtle.pendown()
    
def esquerda():
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(50)
    turtle.pendown()

def direita():
    turtle.penup()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.pendown()

def Circulo():
    turtle.circle(50)
    
def Quadrado():
    for q in range (4):
        turtle.forward(100)
        turtle.left(90) 

def Triangulo():
    for q in range (3):
        turtle.forward(100)
        turtle.left(120)
       
turtle.listen()

turtle.onkey(cima, 'Up')
turtle.onkey(baixo, 'Down')
turtle.onkey(esquerda, 'Left')
turtle.onkey(direita, 'Right')
turtle.onkey(Circulo, 'c')
turtle.onkey(Quadrado, 'q')
turtle.onkey(Triangulo, 't')

turtle.done()
