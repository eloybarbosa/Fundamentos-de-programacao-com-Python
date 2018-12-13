#07. Usando a biblioteca ‘pygame’, escreva um programa que desenha na tela em posição aleatória um quadrado amarelo de tamanho 50 (cinquenta), toda vez que a tecla espaço for pressionada ou o botão direito for clicado.

import pygame
import random

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)
amarelo = (255,255,0)

pygame.init()
tela = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Atividade 07")
relogio = pygame.time.Clock()
tela.fill(preto)
terminou = False



def quadrado_amarelo():
    x = random.randint(25, 615)
    y = random.randint(25, 455)
    pygame.draw.rect(tela, amarelo, (x, y, 50, 50))

    
    
while not terminou:
   
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  terminou = True
          
          if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_SPACE:
                  quadrado_amarelo()
          
          if event.type == pygame.MOUSEBUTTONDOWN:
              quadrado_amarelo()
    
    pygame.display.update()
    relogio.tick(27)
    
pygame.display.quit()

pygame.quit()
