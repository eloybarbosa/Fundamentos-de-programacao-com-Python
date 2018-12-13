#06. Escreva uma função em Python que leia uma tupla contendo números inteiros, retorne uma lista contendo somente os números ímpares e uma nova tupla contendo somente os elementos nas posições pares.

print('Nesta atividade vamos criar uma Tupla contendo 5 números INTEIROS, depois vamos retornar uma lista contendo somente os números ímpares e uma Nova Tupla contendo somente os elementos nas posições pares.')
print()
print('Lembrando que ao retornar os elementos nas posições pares iremos considerar o indice da Tupla criada que inicia em "0" OBS.: Nessa atividade o "0" será considerado como par.')
print()

tupla =()
lista_impar= []
i=1
tupla_par = ()

n = int(input("Entre com o primeiro número: "))
tupla +=(n,)
for c in range(1, 5):
    
    n = int(input("Entre com o próximo número: "))
    tupla +=(n,)
    c += 1

tamanho_tupla = len(tupla)

for p in range (0, tamanho_tupla, 2):
    tupla_par += (tupla[p],)
   
for i in range (0, tamanho_tupla):
    if tupla[i] % 2 != 0:
        lista_impar.append(tupla[i])
   
print()
print('A nossa lista somente com números ímpares da Tupla inicial ficou da seguinte forma: ', lista_impar)

print()
print('A nossa nova tupla somente com os elementos que estão nas posições pares ficou da seguinte forma: ', tupla_par)


    
