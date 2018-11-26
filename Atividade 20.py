#20. Baseando no código criado na questão anterior, crie uma função na qual dado um N obtido através do usuário, sua tartaruga gire 90 + N graus. Teste para 1, 4 e 10 para obter as figuras a seguir

import turtle

def tartaruga():
    
    turtle.shape('turtle')
    turtle.speed(1000)
    turtle.color('red')
    for q in range(1,n):
        turtle.forward(q)
        turtle.left(90+1)
    turtle.done()
    
def tartaruga4():
    
    turtle.shape('turtle')
    turtle.speed(1000)
    turtle.color('red')
    for q in range(1,n):
        turtle.forward(q)
        turtle.left(90+4)
    turtle.done()
    
def tartaruga10():
    
    turtle.shape('turtle')
    turtle.speed(1000)
    turtle.color('red')
    for q in range(1,n):
        turtle.forward(q)
        turtle.left(90+10)
    turtle.done()



n =int(input('De um valor N para definir o tamanho do desenho:'))

a= int(input('Deseja testar o desenho 1, 4 ou 10? '))

if a == 1:
    tartaruga()
if a == 4:
    tartaruga4()
if a == 10:
    tartaruga10()
else:
    print('Não foi digitado um valor válido.')

