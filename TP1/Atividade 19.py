#19. Dado um valor N do usuário, desenhe com a ferramenta turtle a seguinte imagem

import turtle

def tartaruga():
    
    turtle.shape('turtle')
    turtle.speed(1000)
    turtle.color('red')
    for q in range(1,n):
        turtle.forward(q)
        turtle.left(90)
    turtle.done()

n =int(input('De um valor N para definir o tamanho do desenho:'))

tartaruga()