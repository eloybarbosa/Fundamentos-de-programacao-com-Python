#13. Usando a biblioteca Pygame, escreva um programa que possui uma função que desenha um círculo verde de 100 px de diâmetro no centro da tela que se inicie o movimento da esquerda para a direita. Sempre que chegar em alguma extremidade, o círculo deve trocar a direção e aumentar a velocidade em 1. (código e printscreen)

import pygame

branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
preto = (0, 0, 0)
amarelo = (255, 255, 0)
teste = [320, 240]
pos_bola = [320, 240]

pygame.init()
tela = pygame.display.set_mode([640, 480])

pygame.display.set_caption("Atividade 12")
relogio = pygame.time.Clock()
terminou = False
esquerda = False
direita= True
velocidade = 5


def circulo_azul():
    pygame.draw.circle(tela, verde, pos_bola, 60)
    
def move_direita():
    pos_bola[0] += velocidade
 
 
def move_esquerda():
    pos_bola[0] += -velocidade
  

      
while not terminou:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              terminou = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direita = not direita

            if event.key == pygame.K_RIGHT:
                esquerda = not esquerda
                
    if pos_bola[0] >= 640:
        direita = False
        esquerda = True
        velocidade += +1
    elif pos_bola[0] <= 0:
        direita = True
        esquerda = False
        velocidade += +1
    
    if not direita:
        move_esquerda()
        
    if not esquerda:
        move_direita()
    
    circulo_azul()
    
    
    pygame.display.update()
    relogio.tick(27)
    tela.fill(branco)
    
while pos_bola[0] == 0:
    direita = True
pygame.display.quit()
pygame.quit()
