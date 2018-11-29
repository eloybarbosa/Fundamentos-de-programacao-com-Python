#3. Escreva uma função em Python que calcule o fatorial de um dado número N usando um for. O fatorial de N=0 é um. O fatorial de N é (para N > 0): N x (N-1) x (N-2) x … x 3 x 2 x 1. Por exemplo, para N=5 o fatorial é: 5 x 4 x 3 x 2 x 1 = 120. Se N for negativo, exiba uma mensagem indicando que não é possível calcular seu fatorial.

print('Nessa atividade vamos calcular seu fatorial de N utilizando o comando For')
n=int(input('Digite o número que deseja calcular seu fatorial:'))

fatorial=1

if n >= 0:
    
    for c in range (1, n+1):
        print(c, end=' ')
        fatorial= fatorial *c
       
    print()
    print('O Fatorial de',n,'é:', fatorial)
    
else:
    print()
    print('Não é possível calcular o Fatorial do número informado.')
    