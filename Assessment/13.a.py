#13. Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
#a. Conte todas as palavras no corpo da página, e indique quais palavras apareceram apenas uma vez.
#b. Conte quantas vezes apareceu a palavra ladies no conteúdo da página

import requests
from bs4 import BeautifulSoup
import re
from collections import Counter
print('Nesta atividade vamos utilizar o requests para obter o conteúdo da seguinte página da Web: http://brasil.pyladies.com/about')
print('E depois vamos informar quantas palavra existem no corpo da página, informar quantas aparecem somente uma vez e por fim vamos exibir todas as palavras que aparecem somenteo uma vez.')
print()

lista=[]

umavez=[]

texto=''

url = "http://brasil.pyladies.com/about/"

html = requests.get(url+"index.html").text 
soup = BeautifulSoup(html,"lxml")

for i in soup.html.find_all('p'):
    texto += i.text

lista=texto.split()

qtd_palavras=len(lista)



dic=Counter (lista)

for k, v in dic.items():
    if v == 1:
        umavez.append(k)
        
qtd_umavez=len(umavez)

print(f'No corpo da página existem no total {qtd_palavras} palavras e {qtd_umavez} aparecem somente uma vez, segue abaixo a relação das palavras que aparecem somente uma vez:')
print()

for k, v in dic.items():
    if v == 1:
        print(k)


    
    


    



