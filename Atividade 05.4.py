#Dada uma tupla, retorne uma nova tupla com todos os elementos invertidos.

print('Nessa atividade vamos criar uma tupla inserindo quanto elemento desejarmos, a tupla e encerrada quando for digitada a palava "sair". ')
print('Depois vamos mostrar a tupla original e uma nova tupla com todos os elementos invertidos ')
print()

t=()
t1=t[::-1]

elemento = input("Entre com o primeiro elemento: ")
while elemento != "sair":
    t+=(elemento,)
    elemento = input("Entre com o próximo elemento: ")
    
t1=t[::-1]

print()
print('Nossa tupla original é a seguinte: ', t)
print()
print('Nova tupla com todos os elementos invertidos: ', t1)
