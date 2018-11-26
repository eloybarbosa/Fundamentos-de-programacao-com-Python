import math
import turtle

#referencia: https://github.com/AllenDowney/ThinkPython/blob/master/code/pie.py
   
def polypie(t, n, r):
    """Draws a pie divided into radial segments.

    t: Turtle
    n: number of segments
    r: length of the radial spokes
    """
    angle = 360.0 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        turtle.left(angle)
        turtle.speed(100)
    turtle.done()
    
        
def isosceles(t, r, angle):
    """Draws an icosceles triangle.

    The turtle starts and ends at the peak, facing the middle of the base.

    t: Turtle
    r: length of the equal legs
    angle: peak angle in degrees
    """
    y = r * math.sin(angle * math.pi / 180)

    turtle.right(angle)
    turtle.forward(r)
    turtle.left(90+angle)
    turtle.forward(2*y)
    turtle.left(90+angle)
    turtle.forward(r)
    turtle.left(180-angle)
    
        

t= int(input('De quantos lados o poligono será composto? (Obrigatóriamente acima de 4 lados.) '))

if t > 4:
    polypie(turtle, t, 100)
else:
    print('Favor executar novamente e digitar um valor maior que 4 conforme solicitado. ')

