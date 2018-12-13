#Obtenha, usando requests ou urllib, dentro de seu programa em Python, o csv do link:
#https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv
#Obtenha, dentre os jogos do gênero de ação (Action), tiro (Shooter) e plataforma (Platform):
#Quais são as três marcas que mais publicaram jogos dos três gêneros combinados? Indique também o total de jogos de cada marca.
#Quais são as três marcas que mais venderam os três gêneros combinados? Indique também o total de vendas de cada marca.
#Qual é a marca com mais publicações em cada um dos gêneros nos últimos dez anos no Japão? Indique também o número total de jogos dela.
#Qual foi a marca que mais vendeu em cada um desses gêneros nos últimos dez anos, no Japão? Indique também o total de vendas dela.

import requests
import re
from bs4 import BeautifulSoup
from collections import Counter

print('Nesta atividade vamos utilizar o requests para obter o conteúdo do seguinte arquivo CSV: https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv')

print('\nE depois vamos obter informações somente dos seguintes generos de jogos:ação (Action), tiro (Shooter) e plataforma (Platform):')

print('\nE dpor fim informar qual as três marcas que mais publicaram jogos dos 3 generos combinados e o total de jogo de cada marca.')


url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'

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

generos = []

for i in range (0, tam_lista):
    temp = lista[i]
    if lista[i][3] == 'Action':
        generos.append(temp[:])
        
    elif lista[i][3] == 'Shooter':
        generos.append(temp[:])
        
    elif lista[i][3] == 'Platform':
        generos.append(temp[:])
    temp.clear()        

tam_generos = len(generos)

lista_limpa=[]

for i in range (tam_generos):
    del(generos[i][10:])
    
total=[]
    
for i in range (tam_generos):
    temp=generos[i]
    total.append(temp[4])
    temp.clear()
    
marcas=sorted(set(total))

marcas_total=[]

for i in range(len(marcas)):
    temp=marcas[i]
    temp2=total.count(temp)
    marcas_total.append(temp2)
    
tresmaiores=sorted(marcas_total, reverse=True)
tresmaiores=tresmaiores[:3]

primeirolugar=marcas_total.index(tresmaiores[0])
primeirolugar=marcas[primeirolugar]
    
segundolugar=marcas_total.index(tresmaiores[1])
segundolugar=marcas[segundolugar]

terceirolugar=marcas_total.index(tresmaiores[2])
terceirolugar=marcas[terceirolugar]


print('\nAs marcas que mais publicaram jogos nos três gêneros em questão foi:\n')
print(f'Em primeiro lugar a {primeirolugar} com {tresmaiores[0]} jogos publicados')
print(f'Em segundo lugar a {segundolugar} com {tresmaiores[1]} jogos publicados')
print(f'Em terceiro lugar a {terceirolugar} com {tresmaiores[2]} jogos publicados')

   
    

##dic = []
##lista_dic=[]
##
###titulo = ['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales', 'Critic_Score', 'Critic_Count', 'User_Score', 'User_Count', 'Developer', 'Rating']
##titulo = ['Nome', 'Plataforma', 'Ano_de_Lançamento', 'Gênero', 'Publicador', 'NA_Vendas', 'EU_Vendas', 'JP_Vendas', 'Outras_Vendas', 'Global_Vendas', 'Critic_Score', 'Critic_Count', 'User_Score','User_Count','Desenvolvedor','Ratio']
##
##for i in range (0, tam_generos):
##    temp=generos[i]
##    dic=dict(zip(titulo, temp))
##    lista_dic.append(dic)
##    temp.clear()
##    

    

    
    
    

    

    