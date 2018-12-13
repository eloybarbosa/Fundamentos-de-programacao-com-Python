#13. Obtenha, usando requests ou urllib, o conteúdo sobre as PyLadies no link http://brasil.pyladies.com/about e:
#b. Conte quantas vezes apareceu a palavra ladies no conteúdo da página

import requests
from bs4 import BeautifulSoup
import re
print('Nesta atividade vamos utilizar o requests para obter o conteúdo da seguinte página da Web: http://brasil.pyladies.com/about')
print('E depois vamos exibir quantas vezes a palavra Ladies apareceu no conteúdo da página seja em maiusculo ou minusculo')

url = "http://brasil.pyladies.com/about/"

minuscula = "ladies"
maiuscula = "Ladies"

html = requests.get(url).text

soup = BeautifulSoup(html, "lxml")
M = len(re.findall(maiuscula, soup.get_text()))
m = len(re.findall(minuscula, soup.get_text()))

print("\nA palavra ", maiuscula, " apareceu no conteúdo da página " ,M, "vezes.")
print("A palavra ", minuscula, " apareceu no conteúdo da página " ,m, "vezes.")
print("No total ela apareceu no texto " ,M+m, "vezes.")
