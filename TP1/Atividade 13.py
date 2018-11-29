#13. Usando a função obtida na questão 10, desenhe n quadrados um dentro de outro como mostrado na figura:

import turtle

turtle.title('Quadrado dentro de quadrado')
turtle.shape('turtle')
turtle.speed('fastest')

for c in range(4):
	turtle.forward(200)
	turtle.left(90)
turtle.forward(120)
turtle.left(90)
turtle.penup()
turtle.forward(40)
turtle.pendown()

for c in range(4):
	turtle.forward(90)
	turtle.left(90)
turtle.forward(60)
turtle.left(90)
turtle.penup()
turtle.forward(30)
turtle.pendown()

for c in range(4):
	turtle.forward(30)
	turtle.left(90)

turtle.forward(20)
turtle.left(90)
turtle.penup()
turtle.forward(10)
turtle.pendown()

for c in range(4):
	turtle.forward(10)
	turtle.left(90)
turtle.done()

