#04. Escreva um programa em Python que leia um vetor de 5 números inteiros e o apresente na ordem inversa. Imprima o vetor no final. Use listas. Exemplo: se a entrada for [4, 3, 5, 1, 2], o resultado deve ser [2, 1, 5, 3, 4].

print('Nessa atividade vamos criar uma lista inserindo 5 números inteiros e vamos apresenta-la na ordem inversa de inserção.')
print()
L = []
T=len(L)
i=0

while True:
    try:
        elemento = int(input("Entre com o primeiro elemento: "))
        L+=[elemento]
    except ValueError:
        print("Favor digitar um núnero inteiro")  
    else:
        break

while True:
    try:
        while i < 4:
            
            elemento = int(input("Entre com o próximo elemento: "))
            i+=1
            L+=[elemento]
    except ValueError:
        print("Favor digitar um núnero inteiro")
        
    else:
        break

L_reversa=L[::-1]

print('\nA lista criada na ordem inversa fica da seguinte forma: ', L_reversa)
