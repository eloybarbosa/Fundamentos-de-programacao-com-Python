#5. Escreva um programa em Python que leia nomes de alunos e suas alturas em metros até que um nome de aluno seja o código de saída “Sair”. O programa deve possuir uma função que indica todos os alunos que tenham altura acima da média (a média aritmética das alturas de todos os alunos lidos). (código)

print('Nesta atividade vamos inserir o nome dos alunos e em seguida a sua altura em metros e depois vamos calcular  a média da altura dos alunos informados e retornar quais são os alunos que tem a altura acima da média.\n OBS.:Quando quiser parar de inserir nomes é só digitar a palavra "Sair".')

temp = []
final = []
soma = 0
acima = []

temp.append(str(input("Insira o nome do primeiro aluno: ")))
while temp[0] != 'sair':
    temp.append(float(input('Agora insira sua altura:')))
    final.append(temp[:])
    temp.clear()
    temp.append(str(input("Insira o nome do próximo aluno: ")))
    
tamanho_final = len(final)

for a in range (0, tamanho_final):
    idade=(final[a][1])
    soma=soma+(final[a][1])
    
media= soma/tamanho_final

for n in range (0, tamanho_final):
    if final[n][1] > media:
       acima.append(final[n][0])

str_acima = ', '.join(acima)
       
print(f'A altura média dos alunos informados é {round(media, 2)}m, os alunos que tem altura acima da média são: {str_acima}')

 

    
    


