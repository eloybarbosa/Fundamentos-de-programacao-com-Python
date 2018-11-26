print('Nessa Atividade vamos desenhar com a ferramenta Turtle um triângulo equilátero de lado "N".')

import turtle
n = int(input('Agora informe o valor de N:'))
turtle.title('Triangulo Equilátero')
turtle.shape('turtle')
for t in range(3):
	turtle.forward(n)
	turtle.left(120)
turtle.done()


