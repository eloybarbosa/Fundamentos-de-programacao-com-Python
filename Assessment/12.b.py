##12. Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
##a.Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
##b.Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.

import requests
from bs4 import BeautifulSoup

print('Nesta atividade vamos obter dados utilizando o requests da seguinte página da web: https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')
print()
print('E depois o usuário vai inserir uma sigla de um estado da região Centro-Oeste e com isso vamos apresentar as informações contidas na tabela sobre esse estado.')
print()
texto=''

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text

soup = BeautifulSoup(html,"lxml")

for i in soup.html.find_all('article'):
    texto += i.text
    lista = (texto.splitlines())

sigla = input('Agora insira a sigla de um estado do Centro-Oeste (DF, GO, MT ou MS) para obter mais informações:')
if sigla not in lista:
    print()
    print('A sigla inserida não corresponde a um estado do Centro-Oeste')
    
else:
    if sigla=='DF' or sigla=='GO' or sigla=='MT' or sigla=='MS':
        resultado = lista[(lista.index(sigla)):(lista.index(sigla)+5)]
        
        print()    
        print(resultado)
        print()
        print( ' '.join(resultado))
        print()
        print('Estado escolhido:', resultado[0],
              '\nNome: ', resultado[1],
              '\nCapital: ', resultado[2],
              '\nPopulação: ', resultado[3],
              '\nÁrea: ', resultado[4])
    else:
        print()
        print('A sigla inserida não corresponde a um estado do Centro-Oeste')





