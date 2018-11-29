#15. Rode o código a seguir e explique com suas palavras o que acontece nele

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
   

def main():
   teste()
   turtle.done()

main()

##O Código tem quatro funções:
##
##A primeira chamada "geraPontos(i)" gera uma 4 tuplas dentro de uma lista que seriam responsaveis para gerar os pontos para criar um quadrado de qualquer tamanho a partir da variavel "i", porém só está sendo chamada para desenhar o quadrado maior.
##
##A segunda chamada "desenhaPoligono" é para pré deteriminar como o poligono será desenhado. dizendo onde deverá ser inserido os valores de x e y para determinar a posição do Poligono, onde deverá entrar a lista com as tuplas para determinar o tamanho e a cor padrão da linha e do recheio caso nenhuma outra cor seja informada. OBS: Só não conseguir entender como foi achado o valor de “d” em dx, dy
##
##A terceira chamada "teste" basicamente determina os poligonos que serão feitos chamando as funções anteriores com algumas particularidades: o unico poligono que ta chamando a função para gerar os pontos para determinar o tamanho é o quadrado maior, o quadrado menor e o triangulo estão definidos manualmente e no quadrado maior e no triangulo está definido que não será usado a cor de linha padrão e  sim a cor verde.
##
##A quarta e ultima é somente para chamar a função teste e desenhar os poligonos na tela e finalizar a ferramente turtle.
##
##e por fim o código do programa se resume em chamar a função main()