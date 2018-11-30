#11. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela que se move da esquerda para a direita. Sempre que chegar na extremidade direita, o círculo deve voltar à extremidade esquerda, retomando o movimento da esquerda para a direita. (código e printscreen)

import pygame

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)
pos_bola = [320, 240]

pygame.init()
tela = pygame.display.set_mode([640, 480])

pygame.display.set_caption("Atividade 11")
relogio = pygame.time.Clock()
terminou = False

def circulo_azul():
    pygame.draw.circle(tela, azul, pos_bola, 60)
    
def movimento():
    pos_bola[0] += 5
    while pos_bola[0] == 640:
        pos_bola[0]=0
        
      
while not terminou:

    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  terminou = True
    
    circulo_azul()
    movimento()  
    
    
    pygame.display.update()
    relogio.tick(60)
    tela.fill(branco)
pygame.display.quit()
pygame.quit()
