print('Nessa atividade vamos receber três valores reais (X, Y e Z) guardalos em uma tupla, verificar se os valores informados podem ser os comprimentos dos lados de um triângulo e se for o caso retornar qual o tipo de triângulo.')
print()
X=int(input('Insira o valor de X:'))
Y=int(input('Insira o valor de Y:'))
Z=int(input('Insira o valor de Z:'))
T=()
T= (X, Y, Z)

if (X>Y+Z) and (Y>Z+X) and (Z>X):
    print('Essas medidas não formam um triângulo')
    
else:
    if (X==Y) and (Y==Z):
        print("De acordo com as medidas informadas o Triangulo é Equilátero")
    elif (X==Y) or (Y==Z) or (X==Z):
        print("De acordo com as medidas informadas o Triangulo é Isósceles")
    elif (X!=Y) and (Y!=Z) and (Z!=X):
        print("De acordo com as medidas informadas o Triangulo é Escaleno")
    
