#10. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um quadrado de lado N.

print('Nessa Atividade vamos desenhar com a ferramenta Turtle um quadrado de lado "N".')

import turtle
n = int(input('Agora informe o valor de N:'))
turtle.title('Quadrado') 
turtle.shape('turtle')
for q in range(4):
	turtle.forward(n)
	turtle.left(90)
turtle.done()


