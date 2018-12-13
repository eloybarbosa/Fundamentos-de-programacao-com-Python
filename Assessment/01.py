#01. Usando o Thonny, escreva um programa em Python que leia uma tupla contendo 3 números inteiros, (n1, n2, n3) e os imprima em ordem crescente.

print('Nessa atividade vamos criar uma tupla inserindo 3 números inteiros e vamos apresenta-la na ordem crescente.')
print()
T = ()
i=0

while True:
    try:
        elemento = int(input("Entre com o primeiro elemento: "))
        T+=(elemento,)
    except ValueError:
        print("Favor digitar um núnero inteiro")  
    else:
        break
while True:
    try:
        while i < 2:
            
            elemento = int(input("Entre com o próximo elemento: "))
            i+=1
            T+=(elemento,)
    except ValueError:
        print("Favor digitar um núnero inteiro")
        
    else:
        break

T_crescente=(sorted(T))

print('\nA tupla criada na ordem crescente ficou da seguinte forma: ', T_crescente)
