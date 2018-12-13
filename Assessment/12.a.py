##12. Obtenha, usando requests ou urllib, a página HTML https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html dentro de seu programa em Python e faça:
##a.Imprima o conteúdo referente apenas à tabela apresentada na página indicada.
##b.Escreva um programa que obtenha do usuário uma sigla do estado da região Centro-Oeste e apresenta suas informações correspondentes na tabela. O resultado deve apresentar apenas o conteúdo, sem formatação. Ou seja, as tags não devem aparecer. Não esqueça de checar se a sigla pertence à região.

import requests
from bs4 import BeautifulSoup


print('Nesta atividade vamos obter dados utilizando o requests da seguinte página da web: https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html')
print()
print('E depois de obter os dados vamos exibir apenas o conteúdo referente à tabela apresentada na pagina indicada')
lista=[]
texto=''

url = "https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html"

html = requests.get(url).text

soup = BeautifulSoup(html,"lxml")

for i in soup.html.find_all('article'):
    texto += i.text
print ()
print('Abaixo segue o apenas o conteúdo da tabela, agrupado linha por linha', texto)




