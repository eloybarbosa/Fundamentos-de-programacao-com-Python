#4. Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente. Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele. (código)

print('Nessa atividade vamos criar um vetor somente de números inteiros com o tamanho a ser definido.\n Primeiro vamos inserir o número tambem inteiro que vai definir o tamanho do nosso vetor.\n Depois de acordo com o tamanho do nosso vetor iremos definir os números que irão definir o vetor um por um.')
print()

vetor=[]
while True:
    try:
        t = int(input('Primeiramente insira o tamanho do vetor: '))
        print()

        print('Muito bom nosso vetor terá', t, 'números inteiros')
        print()
        
        for i in range (0, t):
            n=int(input('Insira os numeros para o vetor:'))
            vetor.append(n)
        
                   
    except ValueError:
        print("Favor digitar um núnero inteiro")
    else:
        break

print()    

print('Nosso vetor ficou da seguinte forma:', vetor)

z=vetor.count(0)
print()     
print('O número 0 apareceu no vetor ', z, ' vezes')
