print('Nessa atividade vamos calcular seu Fatorial de N utilizando o comando While')
n=int(input('Digite o número que deseja calcular seu Fatorial:'))

contador = n
resultado = 1
if n >= 0:
    while contador > 0:
        #print(contador, end=' ')
        resultado = resultado * contador
        contador = contador-1
        
    print('O Fatorial de',n,'é:',resultado)
else:
    print()
    print('Não é possível calcular o Fatorial do número informado.')
    
    
   
    

