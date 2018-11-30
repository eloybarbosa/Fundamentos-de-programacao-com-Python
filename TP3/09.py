#9. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)

import pygame

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)

pygame.init()
tela = pygame.display.set_mode([640, 480])
tela.fill(branco)
pygame.display.set_caption("Atividade 9")
relogio = pygame.time.Clock()
relogio.tick(27)
terminou = False

def circulo_azul():
    pygame.draw.circle(tela, azul, (320, 240), 50) 

      
while not terminou:
    pygame.display.update()
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  terminou = True
    circulo_azul()                 


pygame.display.quit()
pygame.quit()
