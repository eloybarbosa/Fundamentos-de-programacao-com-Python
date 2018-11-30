#12. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo amarelo de 100 px de diâmetro no centro da tela que se move sempre em velocidade permanente na direção que o usuário indicar através das teclas. Similar ao item anterior, sempre que chegar em uma extremidade, o círculo deve voltar à extremidade oposta e continuar o com a última direção que o usuário indicou. (código e printscreen)

import pygame

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)
amarelo = (255, 255, 0)

pos_bola = [320, 240]

pygame.init()
tela = pygame.display.set_mode([640, 480])

pygame.display.set_caption("Atividade 12")
relogio = pygame.time.Clock()
terminou = False
esquerda = True
direita= True

def circulo_azul():
    pygame.draw.circle(tela, amarelo, pos_bola, 60)
    
def move_direita():
    pos_bola[0] += +5
    while pos_bola[0] == 640:
        pos_bola[0]=0 
        
def move_esquerda():
    pos_bola[0] += -5
    while pos_bola[0] == 0:
        pos_bola[0]=640        
        
    

      
while not terminou:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              terminou = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direita = not direita
            
            if event.key == pygame.K_RIGHT:
                esquerda = not esquerda
              
    
    
    if not direita:
        move_esquerda()
        
    if not esquerda:
        move_direita()
    
    circulo_azul()
    
    
    pygame.display.update()
    relogio.tick(27)
    tela.fill(branco)
pygame.display.quit()
pygame.quit()
