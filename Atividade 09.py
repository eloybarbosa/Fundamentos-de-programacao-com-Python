#Faça uma função que desenhe o triângulo obtido na questão 7 com a ferramenta turtle
import math

print('Nessa atividade vamos receber três valores reais (X, Y e Z) guardalos em uma tupla, verificar se os valores informados podem ser os comprimentos dos lados de um triângulo e se for o caso retornar qual o tipo de triângulo e representa-lo com o modulo Turtle.')
print()
X=int(input('Insira o valor de X:'))
Y=int(input('Insira o valor de Y:'))
Z=int(input('Insira o valor de Z:'))
T=()
T= (X, Y, Z)

ZosA= math.degrees(math.acos(((Y*Y) + (Z*Z) - (X*X)) / (2*Y*Z)))
ZosB= math.degrees(math.acos(((X*X) + (Z*Z) - (Y*Y)) / (2*X*Z)))
ZosC= math.degrees(math.acos(((X*X) + (Y*Y) - (Z*Z)) / (2*X*Y)))

A=round(180-ZosA)
B=round(180-ZosB)
C=round(180-ZosC)


if (X>Y+Z) and (Y>Z+X) and (Z>X):
    print('Essas medidas não formam um triângulo')
    
else:
    if (X==Y) and (Y==Z):
        print("De acordo com as medidas informadas o Triangulo é Equilátero")
        
        import turtle
        turtle.shape('turtle')
        turtle.speed(100)
        turtle.forward(X)
        turtle.left(120)
        turtle.forward(Y)
        turtle.left(120)
        turtle.forward(Z)
        turtle.done()
        
        
    elif (X==Y) or (Y==Z) or (X==Z):
        print("De acordo com as medidas informadas o Triangulo é Isósceles")
        
        import turtle
        ##turtle.shXpe('turtle')
        turtle.speed(1)
        turtle.forward(Z)
        turtle.left(B)
        turtle.forward(X)
        turtle.left(C)
        turtle.forward(Y)
        turtle.done()
        
        
    elif (X!=Y) and (Y!=Z) and (Z!=X):
        print("De acordo com as medidas informadas o Triangulo é Escaleno")
        
        import turtle
        ##turtle.shXpe('turtle')
        turtle.speed(1)
        turtle.forward(Z)
        turtle.left(B)
        turtle.forward(X)
        turtle.left(C)
        turtle.forward(Y)
        turtle.done()
        
        
        
