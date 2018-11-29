print('Nessa atividade vamos criar uma tupla inserindo quanto elemento desejarmos, a tupla e encerrada quando for digitada a palava "sair". ')
print('Depois o programa vai nos retornar 2 tuplas onde cada uma representa uma metade da tupla original. ')
print()

t=()
i=0
t1=()
t2=()

while i % 2 == 0:
    print('A tupla precisa obrigatóriamente de um numero par de elementos')
    t= ()
##  len(t) = (len(t))+1
    elemento = input("Entre com o primeiro elemento: ")
    while elemento != "sair":
        t+=(elemento,)
        elemento = input("Entre com o próximo elemento: ")
    i=len(t)
    i=i+1
    
    
##print(len(t))
r=int(len(t)/2)
##print(r)
print()
t1=(t[:r])
print('A primeira metade da tupla é: ',t1)

t2=(t[-r:])
print('A segunda metade da tupla é:',t2)





##for i1 in range (0,r):
##    print(i1, end=' ')
##    

##t = (10, 20, 30, 40)
##
##t1 = (t[0], t[1])
##
##t2 = (t[2], t[3])
##
##print(len(t))
##
