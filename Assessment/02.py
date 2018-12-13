#02. Usando o Thonny, escreva um programa em Python que some todos os números pares de 1 até um dado n, inclusive. O dado n deve ser obtido do usuário. No final, escreva o valor do resultado desta soma.

print('Nessa atividade vamos somar todos os números pares de 1 ate N')

n=int(input("Insira o valor de N:"))
print('Agora vamos somar todos os numeros pares de 1 até', n)

resultado = 0
contador = 0

for c in range(0, n+1, 2):
    print(c, end=' ')
    resultado = resultado + c
    contador = contador + 1
       
print()    
print('No intervalo entre 1 e',n,'temos',contador-1,'números pares, e a soma de todos os números resulta em',resultado)