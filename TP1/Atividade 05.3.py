#5.3 Dada uma tupla e um elemento, elimine esse elemento da tupla.

print('Nessa atividade vamos criar uma tupla inserindo quanto elemento desejarmos, a tupla e encerrada quando for digitada a palava "sair". ')
print('Depois vamos indicar um dos elementos da tupla para ser "eliminado"')
print()

t = ()
t1= ()
r=0
q=0

elemento = input("Entre com o primeiro elemento: ")
while elemento != "sair":
    t+=(elemento,)
    elemento = input("Entre com o próximo elemento: ")
  

print(t)
print()

i=(input('Agora indique um dos elementos inseridos para que o mesmo seja "eliminado" da tupla:'))

while i not in t:
    print('Você não pesquisou por um elemento inserido anteriormente.')
    i=(input('Tente novamente:'))

print('O indice do elemento "', i, '" é:',t.index(i))

r=t.index(i)

q=len(t)

qq=q-1

if r == 0:
    t1=(t[r+1:])
    
elif r == qq:
    t1=(t[:r])
       
elif r == r:
    t1=(t[:r]+t[-(-r+qq):])
    
print(t1)


    
