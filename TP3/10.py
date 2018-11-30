#9. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo azul de 100 px de diâmetro no centro da tela. (código e printscreen)

import pygame

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)

pos_x=10
pos_y=10


pygame.init()
tela = pygame.display.set_mode([640, 480])

pygame.display.set_caption("Atividade 9")
relogio = pygame.time.Clock()

terminou = False

def quadrado_vermelho():
    pygame.draw.rect(tela, vermelho, (pos_x, pos_y, 100, 100))  


while not terminou:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x += -10
            if event.key == pygame.K_RIGHT:
                pos_x += 10
            if event.key == pygame.K_UP:
                pos_y += -10
            if event.key == pygame.K_DOWN:
                pos_y += 10
    
    quadrado_vermelho()
    
    pygame.display.update()
    relogio.tick(50)
    tela.fill(branco)
pygame.display.quit()
pygame.quit()


