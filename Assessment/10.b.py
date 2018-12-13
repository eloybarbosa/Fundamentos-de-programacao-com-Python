#10.b.Para cada esporte, considere todas as modalidades, tanto no masculino quanto no feminino. Sua resposta deve imprimir um relatório mostrando o total de medalhas de cada um dos países e em que esporte, ano, cidade e gênero (masculino ou feminino) cada medalha foi obtida.

import requests
import json
from collections import Counter


url = "https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv"
conn = requests.Session().get(url)

if conn.status_code != 200:
    conn.raise_for_status()
else:
    print("Conectado com sucesso!")

rows = [data.split(",") for data in conn.text.split("\n")]

header = rows.pop(0)
lister = []

for row in rows:
    lister.append({header[index]: item for index, item in enumerate(row)})

def relatorio(json_Format=False):
    CountMedal = dict(Counter([item["NOC"] for item in lister]))

    talkative = {}

    for key in CountMedal.keys():
        talkative[key] = {}
        talkative[key]["Total de Medalhas"] = CountMedal[key]

    for key in talkative.keys():
        talkative[key]["Medalhas"] = []

        for medal in [item for item in lister if item["NOC"] == key]:
            medalRows = {"Esporte": medal["Sport"], "Ano": medal["Year"], "Cidade": medal["City"], "Genero": "Masculino" if medal["Event gender"] == "M" else "Femenino"}

        talkative[key]["Medalhas"].append(medalRows)

    if json_Format:
        print(json.dumps(talkative, indent=1))

    else:
        for country in talkative.keys():
            print("\n")
            print('Total de Medalhas: %d' % talkative[country]['Total de Medalhas'])

            defaultForms = "{:<14}{:<6}{:<10}{:<22}"
            print(defaultForms.format('Esporte', 'Ano', 'Genero', 'Cidade', 'Pais'))
            for medals in talkative[country]['Medalhas']:
                print(defaultForms.format(medals['Esporte'], medals['Ano'], medals['Genero'], medals['Cidade']))

print('\nNesta atividade vamos exibir um relatório mostrando o total de medalhas de cada um dos países dividido por esporte, ano, cidade e gênero.\n')
print('\n============= RELATÓRIO =============')
relatorio()