#10. Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
#https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv
#E:
#a -  Dentre os seguintes países nórdicos: Suécia, Dinamarca e Noruega, verifique: No século XXI (a partir de 2001), qual foi o maior medalhista de ouro, considerando apenas as seguintes modalidades:
#I - Curling
#II - Patinação no gelo (skating)
#III - Esqui (skiing)
#IV - Hóquei sobre o gelo (ice hockey)

import requests
import re
from bs4 import BeautifulSoup
import pprint

print('Nesta atividade vamos utilizar o requests para obter o conteúdo do seguinte arquivo CSV: https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv')

print('\nE depois vamos exibir dentre os tres países nórdicos: Suécia, Dinamarca e Noruega , a partir do Século XXI, qual foi o maior medalhista considerando apenas as seguintes modalidades: Curling, Skatin, Skiing e Ice Hockey')


url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'

conn = requests.get(url, timeout=5)

if conn.status_code != 200:
	conn.raise_for_status()
else:
	print("Conectado com sucesso!")

csv = requests.get(url).text

csv_lista = csv.splitlines()

tam_csv_lista = len(csv_lista)

lista=[]

for i in range(1, tam_csv_lista):
    temp = csv_lista[i].split(',')
    lista.append(temp[:])
    temp.clear()
    
tam_lista = len(lista)

lista_ano=[]

for i in range (0, tam_lista):
    temp = lista[i]
    if lista[i][0] == '2001' or lista[i][0] == '2002' or lista[i][0] == '2003' or lista[i][0] == '2004' or lista[i][0] == '2005' or lista[i][0] == '2006':
        lista_ano.append(temp[:])
        temp.clear()
        
tam_lista_ano= len(lista_ano)

nordicos = [] #noruega, suecia, dinamarca

for i in range (0, tam_lista_ano):
    temp = lista_ano[i]
    if lista_ano[i][4] =='NOR':
        nordicos.append(temp[:])
        temp.clear()
        
    elif lista_ano[i][4] =='SWE':
        nordicos.append(temp[:])
        temp.clear()

    elif lista_ano[i][4] =='DEN':
        nordicos.append(temp[:])
        temp.clear()
        
tam_nordicos = len(nordicos)

gold = []

for i in range (0, tam_nordicos):
    temp = nordicos[i]
    if nordicos[i][7] =='Gold':
        gold.append(temp[:])
        temp.clear()

tam_gold = len(gold)

esportes = []

for i in range (0, tam_gold):
    temp = gold[i]
    if gold[i][2] == 'Curling':
        esportes.append(temp[:])
        temp.clear()
        
    elif gold[i][2] == 'Skating':
        esportes.append(temp[:])
        temp.clear()
    
    elif gold[i][2] == 'Skiing':
        esportes.append(temp[:])
        temp.clear()
        
    elif gold[i][2] == 'Ice Hockey':
        esportes.append(temp[:])
        temp.clear()
    
tam_esportes = len(esportes)

nor = 0
swe = 0
den = 0

for i in range (0, tam_esportes):
    if esportes[i][4] == 'NOR':
        nor += 1
        
for i in range (0, tam_esportes):
    if esportes[i][4] == 'SWE':
        swe += 1
        
for i in range (0, tam_esportes):
    if esportes [i][4] == 'DEN':
        den += 1
        
print(f'\nO maior medalhista de Ouro, considerando apenas as modalidades citadas é a Noruega com {nor} medalhas de ouro.')
print(f'\nJá o segundo colocado foi a Suécia com {swe} medalhas de ouro.' )
print(f'\nNo arquivo de consulta que nos foi passado não havia registros da Dinamarca.')