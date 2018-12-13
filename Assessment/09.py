#08. Usando o código anterior, escreva um novo programa que, quando as teclas ‘w’, ‘a’, ‘s’ e ‘d’ forem pressionadas, ele movimente o círculo com o texto “clique” nas direções corretas. Caso colida com algum retângulo, o retângulo que participou da colisão deve desaparecer.

import pygame
import random
import math

largura = 640
altura = 480


branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (155, 0, 0)
azul = (0, 255, 255)
verde = (0, 255, 0)
amarelo = (255, 255, 0)

pygame.init()
pygame.display.set_caption('9')

fonte = pygame.font.SysFont('Courrier New', 21)
tela = pygame.display.set_mode((largura, altura))
clock = pygame.time.Clock()
fim = False

quadrados = []

circulo = {"x": 60, "y": 60, "raio": 50, "dir": None, "speed": 10}


def circulo_vermelho():
    pygame.draw.circle(tela, vermelho, (circulo["x"], circulo["y"]), circulo['raio'])
    textsurface = fonte.render("Clique", False, branco)
    tela.blit(textsurface, (circulo["x"] - 25, circulo["y"] - 10))


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


def mover_circulo():
    if circulo["dir"] is None:
        return

    circulo["x"] += int(math.cos(math.radians(circulo["dir"])) * circulo["speed"])
    circulo["y"] -= int(math.sin(math.radians(circulo["dir"])) * circulo["speed"])

    for quadrado in quadrados:
        if checa_colisao((quadrado[0], quadrado[1], 100, 50), (circulo["x"], circulo["y"], circulo["raio"])):
            quadrados.remove(quadrado)


def checa_colisao(rect, circle):
    def dentro_circle(ponto):
        dist = math.sqrt((circle[0] - ponto[0]) ** 2 + (circle[1] - ponto[1]) ** 2)
        if dist <= circle[2]:
            return True, dist
        return False, dist

    def dentro_rect(ponto):
        if ((rect[0] <= ponto[0] <= rect[0] + rect[2]) and
                (rect[1] <= ponto[1] <= rect[1] + rect[3])):
            return True
        return False

    pontos_rect = ((rect[0], rect[1]),
                   (rect[0] + rect[2], rect[1]),
                   (rect[0], rect[1] + rect[3]),
                   (rect[0] + rect[2], rect[1] + rect[3]))

    pontos_circle = ((circle[0] + circle[2], circle[1]),
                     (circle[0], circle[1] + circle[2]),
                     (circle[0] - circle[2], circle[1]),
                     (circle[0], circle[1] - circle[2]))

    # distancia minima para alguma aresta encostar, maior q isso esta
    # longe o suficiente para ignorar
    minima_dist = circle[2]*2 + (rect[2] if rect[2] > rect[3] else rect[3])

    for ponto_circle in pontos_circle:
        if dentro_rect(ponto_circle):
            return True

    for ponto_rect in pontos_rect:
        result = dentro_circle(ponto_rect)
        if result[0]:
            return True
        elif result[1] > minima_dist:
            return False

    return False

while not fim:
    # configurando o clock para 30 vezes por segundo
    clock.tick(30)

    tela.fill(preto)

    for x, y in quadrados:
        pygame.draw.rect(tela, amarelo, (x, y, 100, 50))

    circulo_vermelho()
    mover_circulo()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            fim = True
            exit(0)
            break

        if event.type == pygame.MOUSEBUTTONDOWN:
            retangulo_amarelo(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                circulo["dir"] = 90

            elif event.key == pygame.K_s:
                circulo["dir"] = 270

            elif event.key == pygame.K_a:
                circulo["dir"] = 180

            elif event.key == pygame.K_d:
                circulo["dir"] = 0

        if event.type == pygame.KEYUP:
            circulo["dir"] = None