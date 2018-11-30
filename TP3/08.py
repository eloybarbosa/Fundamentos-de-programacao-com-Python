#8. Faça uma função um programa em Python que simula um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor. Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de Python para gerar números aleatórios, simulando os lançamentos dos dados. (código)
import random

print('Nesta atividade vamos simular o lançamento de um dado 100 vezes e depois vamos mostrar quantas vezes cada valor foi conseguido durante a simulação.')
print()
dado = []
dado_lancado=[]
for d in range (1, 7):
    dado.append(d)

for c in range (0, 100):
    lancado=random.choice(dado)
    dado_lancado.append(lancado)

for i in range (1, 7):
    print('O número', i, 'foi conseguido', dado_lancado.count(i), 'vezes.')
    