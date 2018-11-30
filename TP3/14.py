#14. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um quadrado de tamanho 50 no centro da tela. Quando o usuário clicar em alguma área da janela, o quadrado deve se mover para a posição clicada. (código e printscreen)

import pygame

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)
pos_inicial = (295, 215)
posicao = (295, 215)

pygame.init()
tela = pygame.display.set_mode([640, 480])
pygame.display.set_caption("Atividade 14")
relogio = pygame.time.Clock()
terminou = False

def quadrado():
    pygame.draw.rect(tela, azul, (pos_inicial[0], pos_inicial[1], 50, 50))
    

def mudar_posicao():
    pos_inicial=posicao

      
while not terminou:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              terminou = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            posicao = pygame.mouse.get_pos()
            pos_inicial=posicao
    
   
    quadrado()
    
    pygame.display.update()
    relogio.tick(27)
    tela.fill(branco)
pygame.display.quit()
pygame.quit()
