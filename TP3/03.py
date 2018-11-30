#3. Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura. (código)

print('Insira 10 palavras para criarmos um vetor')
print()

vetor10 = []

for i in range (0, 10):
    palavra=str(input('Insira as palavras para o vetor:'))
    vetor10.append(palavra)
    
vetor10_reverso=vetor10[::-1]
print()
print('O nosso vetor de 10 palavras na ordem inversa de leitura ficaria assim:', vetor10_reverso)
    
    
    
    