print('Nessa atividade vamos calcular seu fatorial de N utilizando o comando For')
n=int(input('Digite o número que deseja calcular seu fatorial:'))

fatorial=1

if n >= 0:
    
    for c in range (1, n+1):
        #print(c, end=' ')
        fatorial= fatorial *c
       
    print()
    print('O Fatorial de',n,'é:', fatorial)
    
else:
    print()
    print('Não é possível calcular o Fatorial do número informado.')
    