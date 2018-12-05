#15. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha na tela um estrela de 5 pontas no tamanho que preferir. (código e printscreen)

import pygame
import math

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)

pygame.init()
tela = pygame.display.set_mode([640, 480])
tela.fill(branco)
pygame.display.set_caption("Atividade 15")
relogio = pygame.time.Clock()
relogio.tick(27)
terminou = False


def estrela():

    pontos = []

    for angulo in range(90, 360 + 90, 360 // 5):
        x_ponto = 320 + math.cos(math.radians(angulo)) * 100
        y_ponto = 240 - math.sin(math.radians(angulo)) * 100
        pontos.append((x_ponto, y_ponto))

    for index, ponto in enumerate(pontos):
        if (index + 2 >= len(pontos)):
            prox_ponto = pontos[abs(index + 2 - len(pontos))]
        else:
            prox_ponto = pontos[index + 2]

        pygame.draw.line(tela, vermelho, ponto, prox_ponto, 5)
    
    
while not terminou:
    pygame.display.update()
    for event in pygame.event.get():
          if event.type == pygame.QUIT:
                  terminou = True
    estrela()                 


pygame.display.quit()
pygame.quit()
