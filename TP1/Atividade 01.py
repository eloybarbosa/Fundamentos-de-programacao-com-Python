#1. Escreva uma função em Python que some todos os números ímpares de 1 até um dado N, inclusive. O número N deve ser obtido do usuário. Ao final, escreva o valor do resultado desta soma.

print('Nessa atividade vamos somar todos os números inteiros ímpares de 1 ate N')

n=int(input("Insira o valor de N:"))
print('Agora vamos somar todos os numeros ímpares de 1 até', n)

resultado = 0
contador = 0

for c in range(1, n+1, 2):
    #print(c, end=' ')
    resultado = resultado + c
    contador = contador + 1
       
print()    
print('No intervalo entre 1 e',n,'temos',contador,'números ímpares, e a soma de todos os números resulta em',resultado)


    

    
    
    
