#12. Faça uma função no Python que, utilizando a ferramenta turtle, desenhe um círculo de raio N.

print('Nessa Atividade vamos desenhar com a ferramenta Turtle um circulo de raio "N".')

import turtle
n = int(input('Agora informe o valor de N:'))
turtle.title('Circulo')
turtle.shape('turtle')
turtle.circle(n)
turtle.done()


