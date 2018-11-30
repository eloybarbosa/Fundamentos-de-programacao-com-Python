#6. Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada. Indique quais frases apresentam a palavra “eu”. (código)

temp = []
frases = []
eu_real=0

print('Nessa atividade vamos inserir varias frases e depois vamos indicar em qual frase a palavra "eu" foi utilizada.')

temp.append(str(input("Insira a primeira frase ")))
while temp[-1] != 'sair':
    temp.append(str(input("Insira a proxima frase: ")))
temp.remove('sair')

tamanho=len(temp)

for c in range (0, tamanho):
    if temp[c].count("eu") !=0:
        frases.append(temp[c])
       
num_frases=len(frases)    

if num_frases !=0:
    print()
    print('As frases na qual a palavra eu foi utilizada são as seguintes:')
    for f in range (0, num_frases):
        print(frases[f])
else:
    print()
    print('Nenhuma Frase com a palavra eu foi inserida')
    