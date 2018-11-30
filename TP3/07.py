#7. Escreva um programa em Python que realiza operações de inclusão e remoção em listas. Seu programa deve perguntar ao usuário qual operação deseja fazer: (código)
#a. Mostrar lista;
#b. Incluir elemento;
#c. Remover elemento;
#d. Apagar todos os elementos da lista.
#Se a opção for a alternativa (a), seu programa deve apenas mostrar o conteúdo da lista. Se a opção for a alternativa (b), seu programa deve pedir o valor do elemento a ser incluído. Se a opção for a alternativa (c), seu programa deve pedir o valor do elemento a ser removido. E se a opção for a alternativa (d), deve-se apenas exibir se a operação foi concluída.

lista=['Primavera', 'Verão', 'Inverno', 'Outono']

print('Nessa atividade temos uma lista pré definida, logo abaixo será mostrada uma lista de opções, favor informar oque deseja fazer!')
print()
print(' a. Mostrar Lista.\n b. Incluir Elemento.\n c. Remover Elemento.\n d. Apagar todos os elementos da lista.')
print()

opcao=str(input('Favor escolha a opção desejada:')).upper()
while opcao !='A' and opcao !='B' and opcao !='C' and opcao !='D':
    opcao=str(input('Favor escolha uma opção válida:')).upper()

if opcao == "A":
    print()
    print('Esta é nossa lista!')
    print(lista)
elif opcao == "B":
    print()
    print('Você escolheu inserir um elemento na lista.')
    print()
    elemento=input('Digite o elemento que deseja inserir na lista:')
    lista.append(elemento)
    
elif opcao == "C":
    print()
    print('Você escolheu remover um elemento da lista')
    remover=input('Insira o elemento que deseja remover da lista.')
    while remover not in lista:
        remover=input('Favor inserir um elemento que esteja na lista')
    lista.remove(remover)
    print(lista)        
    
elif opcao == "D":
    lista.clear()
    print()
    print('Você removeu todos os elementos da lista.')
else:
    print()
    print('Você não escolheu uma opção válida, execute novamente.')

