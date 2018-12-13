#03. Usando o Thonny, escreva uma função em Python chamada potencia. Esta função deve obter como argumentos dois números inteiros, A e B, e calcular AB usando multiplicações sucessivas (não use a função de python math.pow) e retornar o resultado da operação. Depois, crie um programa em Python que obtenha dois números inteiros do usuário e indique o resultado de AB usando a função.

def potencia (a, b):
    R = a
    for i in range (1, b):
        R*=a
    return R

print('Nesta atividade vamos informar dois números inteiros "A" e "B" e a partir desses números vamos calcular o valor de A elevado B. (Favor limitar-se a números menores que 100)')
a=int(input('Insira o valor de A:'))
b=int(input('Insira o valor de B:'))

print('O resultado de', a, 'elevado a', b,'é:', potencia (a, b))