#08. Usando a biblioteca ‘pygame’, escreva um programa que desenha um botão (círculo) com o texto “clique” sobre ele na parte superior da tela. Quando o botão for clicado, ele deve chamar uma função que desenha um retângulo em uma posição aleatória na tela. Caso um retângulo apareça na mesma posição que um já existente, ambos devem ser eliminados.

import pygame
import random
import math

largura = 640
altura = 480
branco = (255,255,255)
preto = (0, 0, 0)
vermelho= (155, 0, 0)
azul = (0, 255, 255)
verde = (0, 255, 0)
amarelo = (255, 255, 0)

pygame.init()
pygame.display.set_caption('Atividade 08')

fonte = pygame.font.SysFont('Courrier ', 21)
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
fim = False

quadrados = []

circulo = {"x": 320, "y": 60, "raio": 50}


def circulo_vermelho():
    pygame.draw.circle(tela, vermelho, (circulo["x"], circulo["y"]), circulo['raio'])
    textsurface = fonte.render("CLIQUE", False, branco)
    tela.blit(textsurface, (292, 52))


def retangulo_amarelo(pos):
    dist = math.sqrt((circulo["x"] - pos[0])**2 + (circulo["y"] - pos[1])**2)
    if dist > circulo["raio"]:
        return

    x = random.randint(0, largura - 100)
    y = random.randint(0, altura - 50)

    for quadrado in quadrados:
        rect1 = pygame.Rect((quadrado[0], quadrado[1], 100, 50))
        rect2 = pygame.Rect((x, y, 100, 50))

        if rect1.colliderect(rect2):
            quadrados.remove(quadrado)
            return

    quadrados.append((x, y))



while not fim:

    clock.tick(30)

    tela.fill(preto)

    for x, y in quadrados:
        pygame.draw.rect(tela, amarelo, (x, y, 100, 50))

    circulo_vermelho()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            fim = True
            exit(0)
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            retangulo_amarelo(pygame.mouse.get_pos())
