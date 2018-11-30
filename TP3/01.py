#1. Usando Python, faça o que se pede (código e printscreen):
#a)	Crie uma lista vazia;
#b)	Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
#c)	Imprima a lista;
#d)	Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
#e)	Imprima a lista modificada;
#f)	Imprima também o tamanho da lista usando a função len();
#g)	Altere o valor do último elemento para 6 e imprima a lista modificada.

lista = []
for i in range(1, 6):
    lista.append(i)

print(lista)
print()
print('Agora vamos remover o elemento 3 e 6 da lista caso eles existam na lista.')
print()
if 3 in lista:
    lista.remove(3)
    print('O elemento 3 foi excluido da lista')
    print()
    
else:
    print('O elemento 3 não existe na lista')
    print()
    
if 6 in lista:
    lista.remove(6)
    print('O elemento 6 foi excluido da lista')
    print()
else:
    print('O elemento 6 não existe na lista')
    print()
    
  
print(lista)
tamanho=len(lista)
print()
print ('O tamanho da lista é de', tamanho, 'elementos')
print()
print('Agora vamos alterar o valor do ultimo elemento da lista para 6.')

lista[-1]=6
print()
print(lista)
