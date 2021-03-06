import turtle
def geraPontos(i):
# """ Gera pontos para quadrados de qualquer tamanho """
    return [(i, 0), (i, i), (0, i), (0, 0)]

def desenhaPoligono(inicio, pontos, corLinha="black", corRecheio="white"):
   turtle.pencolor(corLinha)
   turtle.fillcolor(corRecheio)

   turtle.penup()

   turtle.goto(inicio)  

   turtle.pendown()
   turtle.begin_fill()

   x, y = inicio

   for ponto in pontos:  
       dx, dy = ponto
       turtle.goto(x + dx, y + dy)
   turtle.goto(inicio)  

   turtle.end_fill()
   turtle.penup()


def teste():
   # Primeiro quadrado
   quadrado = [(50, 0), (50, 50), (0, 50), (0, 0)]
   desenhaPoligono((200, 200), quadrado)

   # Segundo quadrado
   quadrado_maior = geraPontos(100)
   desenhaPoligono((-200, 200), quadrado_maior, corLinha="green")

   # Triangulo
   triangulo = [(200, 0), (100, 100), (0, 0)]
   desenhaPoligono((100, -100), triangulo, corLinha="green")
   
   # Retangulo
   retangulo = [(300, 0), (300, 150), (0, 150), (0, 0)] #geraPontos(200) #[(x, y), (0, 150), (150, 300), (0, 0)]
   desenhaPoligono((-300, -100), retangulo, corRecheio="green") # ( (x(horizontal, y(vertical)), (chama o objeto))
   
   # Retangulo
   losango = [(150, -80), (0, -150), (-150, -80), (0, 0)] #geraPontos(200) #[(x, y), (0, 150), (150, 300), (0, 0)]
   desenhaPoligono((-150, 50), losango, corRecheio="yellow") # ( (x(horizontal, y(vertical)), (chama o objeto))
   

def main():
   teste()
   turtle.done()

main()