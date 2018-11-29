#17. Escreva uma função que receba uma string e um número inteiro x e rotacione a string x posições para a esquerda. Assuma que a string tem pelo menos x caracteres.

print('Nesta atividade vamos inserir uma palavra qualquer com no minimo 3 caracteres e depois vamos rotacionar essa palavra de acordo com o valor de N')
print('O valor de N tem que ser obrigátoriamente menor do que a quantidade de caracteres da palavra escolhida.')

print()
palavra=str(input('Insira a palavra que deseja usar: '))
print()

lista_palavra=list(palavra)
tamanho_palavra=len(lista_palavra)
nova_lista=[]

if tamanho_palavra >= 3:
    n=int(input('Insira o valor de N: '))
    
    if n <= tamanho_palavra-1:
        
        for i in range(n, tamanho_palavra):
            nova_lista += lista_palavra[i]
            
        for j in range(0, n):
            nova_lista += lista_palavra[j]
    
        nova_palavra = ''.join(nova_lista)
        print('A palavra rotacionada de acordo com o valor de N ficou da seguinte forma: ', nova_palavra)
        
            
    else:
        print('O Valor de N não pode ser maior ou igual ao número de caracteres da palavra escolhida, execute novamente.')
else:
    print('Conforme solicitado a palavra tem que ter mais de 3 caracteres, execute novamente.')
