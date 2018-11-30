#2. Escreva um programa em Python que leia um vetor de 5 números inteiros e mostre-os. (código)

print('Insira 5 números para criarmos nosso vertor')

vetor=[]
i=0

for i in range (0, 5):
    n=int(input('Insira os numeros para o vetor:'))
    vetor.append(n)
    
print()    
print('Nosso vetor ficou da seguinte forma:', vetor)