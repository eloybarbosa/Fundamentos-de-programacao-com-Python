#2. Faça uma função em Python que receba do usuário a idade de uma pessoa em anos, meses e dias e retorne essa idade expressa em dias. Considere que todos os anos têm 365 dias.

print('Nessa atividade vamos descobrir quantos dias voce tem de vida (Considerando que todos os anos tem 365 dias e todos os meses tem 30 dias)')
print()

ano=int(input('Insira o ano do seu nascimento:'))
mes=int(input('Insira o mes do seu nascimento:'))
dia=int(input('Insira o dia do seu nascimento:'))

#https://pythonhelp.wordpress.com/2011/11/05/obtendo-a-data-e-a-hora-atuais-em-python/
from datetime import datetime
now = datetime.now()

diferencaano=now.year-ano
diferencames=now.month-mes
diferencadia=now.day-dia

resultado=((diferencaano*365)+(diferencames*30)+diferencadia)

print()
print('De acordo com a data de nascimento fornecida e com as considerações que foram feitas você tem',resultado,'dias de vida')


