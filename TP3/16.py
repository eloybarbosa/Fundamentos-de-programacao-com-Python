#16. Usando a biblioteca Pygame, escreva um programa que desenha na tela estrelas de 5 pontas de tamanhos aleatórios a cada vez que o usuário clicar na tela. A ponta superior da estrela deve estar situada onde o usuário clicou. (código e printscreen)

import pygame
import math
import random

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)
pos_inicial = (295, 215)
posicao = (295, 215)

pygame.init()
tela = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Atividade 17")
relogio = pygame.time.Clock()
terminou = False

tamanho = random.randint(50, 150)

estrelas = []

def star(estrela):
    pontos = []

    for angulo in range(90, 360 + 90, 360 // 5):
        x_ponto = estrela["pos"][0] + math.cos(math.radians(angulo)) * estrela["size"]
        y_ponto = estrela["pos"][1] - math.sin(math.radians(angulo)) * estrela["size"]
        pontos.append((x_ponto, y_ponto))

    for index, ponto in enumerate(pontos):
        if (index + 2 >= len(pontos)):
            prox_ponto = pontos[abs(index + 2 - len(pontos))]
        else:
            prox_ponto = pontos[index + 2]

        pygame.draw.line(tela, vermelho, ponto, prox_ponto, 5)


def add_star(pos):
    size = random.randint(50, 150)
    pos = list(pos)
    pos[1] += size
    estrelas.append({"pos": pos, "size": size})

def mudar_posicao():
    pos_inicial=posicao

      
while not terminou:
    relogio.tick(27)
    for estrela in estrelas:
        star(estrela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              terminou = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            add_star(pygame.mouse.get_pos())
            posicao = pygame.mouse.get_pos()
            pos_inicial=posicao
    
   
    pygame.display.update()
    
    tela.fill(branco)
pygame.display.quit()
pygame.quit()
