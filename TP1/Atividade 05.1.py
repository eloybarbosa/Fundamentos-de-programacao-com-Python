#5.1. Dada uma tupla e um elemento, verifique se o elemento existe na tupla e retorne o índice do mesmo

print('Nessa atividade vamos criar uma tupla inserindo quanto elemento desejarmos, a tupla e encerrada quando for digitada a palava "sair". ')
print('Depois vamos perquisar por um dos elementos inseridos anteriormente e o programa vai nos retornar o indice do mesmo.')
print()

t = ()
elemento = input("Entre com o primeiro elemento: ")
while elemento != "sair":
    t+=(elemento,)
    elemento = input("Entre com o próximo elemento: ")
  
print()

i=(input('Agora pesquise o elemento que deseja descobrir o indice.'))

while i not in t:
        print('Você não pesquisou por um elemento inserido anteriormente.')
        i=(input('Tente novamente:'))

print('O indice do elemento "', i, '" é:',t.index(i))


    
