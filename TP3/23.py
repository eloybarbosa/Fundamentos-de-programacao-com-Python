#23. (Desafio) Usando a biblioteca Pygame, escreva um programa que implemente o jogo da velha para dois jogadores (ambos usuários). (código e printscreen

import pygame

vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,255)
azulescuro = (0,0,128)
branco = (255,255,255)
preto = (0,0,0)
rosa = (255,200,200)

pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Jogo da Velha')
clock = pygame.time.Clock()
terminou = False

estado = 'jogando'
vez = 'jogador1'
escolha= 'X'
espaco=0

marca_tabu = [
    0, 1, 2,
    3, 4, 5,
    6, 7, 8
    ]

rect1 = pygame.Rect ((0, 0), (200, 200))
rect2 = pygame.Rect ((200, 0), (200, 200))
rect3 = pygame.Rect ((400, 0), (200, 200))
rect4 = pygame.Rect ((0, 200), (200, 200))
rect5 = pygame.Rect ((200, 200), (200, 200))
rect6 = pygame.Rect ((400, 200), (200, 200))
rect7 = pygame.Rect ((0, 400), (200, 200))
rect8 = pygame.Rect ((200, 400), (200, 200))
rect9 = pygame.Rect ((400, 400), (200, 200))

rec = [ rect1, rect2, rect3,
        rect4, rect5, rect6,
        rect7, rect8, rect9
        ]

           

def desenhar_tabu():
    pygame.draw.line(tela, branco, (200, 0), (200, 600), 10)
    pygame.draw.line(tela, branco, (400, 0), (400, 600), 10)
    pygame.draw.line(tela, branco, (0, 200), (600, 200), 10)
    pygame.draw.line(tela, branco, (0, 400), (600, 400), 10)


def desenhar_peca(pos):
    global vez
    x, y = pos
    if vez == 'jogador2':
        pygame.draw.circle(tela, azul, pos, 50)
    else:
        img = pygame.image.load('x.png').convert_alpha()
        imgR = pygame.transform.scale(img, (100, 100))
        tela.blit(imgR, (x - 50, y - 50))
      

def testa_pos():
    for p in rec:
        if event.type == pygame.MOUSEBUTTONDOWN and p.collidepoint(mouse_pos):
            if p == rect1:
                confirmar(0, [100, 100])
            if p == rect2:
                confirmar(1, [300, 100])
            if p == rect3:
                confirmar(2, [500, 100])
            if p == rect4:
                confirmar(3, [100, 300])
            if p == rect5:
                confirmar(4, [300, 300])
            if p == rect6:
                confirmar(5, [500, 300])
            if p == rect7:
                confirmar(6, [100, 500])
            if p == rect8:
                confirmar(7, [300, 500])
            if p == rect9:
                confirmar(8, [500, 500])
                
def confirmar(indice, pos):
    global escolha, vez, espaco
    if marca_tabu[indice] == 'X':
        print('X')
    elif marca_tabu[indice] == 'O':
        print('O')
    else:
        marca_tabu[indice] = escolha
        desenhar_peca(pos)
        print(marca_tabu)
        if vez == 'jogador1':
            vez = 'jogador2'
        else:
            vez = 'jogador1'
        espaco+=1
            
def teste_vitoria(l):
    return ((marca_tabu[0] == l and marca_tabu[1] == l and marca_tabu[2] == l) or
            (marca_tabu[3] == l and marca_tabu[4] == l and marca_tabu[5] == l) or
            (marca_tabu[6] == l and marca_tabu[7] == l and marca_tabu[8] == l) or
            (marca_tabu[0] == l and marca_tabu[3] == l and marca_tabu[6] == l) or
            (marca_tabu[1] == l and marca_tabu[4] == l and marca_tabu[7] == l) or
            (marca_tabu[2] == l and marca_tabu[1] == l and marca_tabu[8] == l) or
            (marca_tabu[0] == l and marca_tabu[4] == l and marca_tabu[8] == l) or
            (marca_tabu[2] == l and marca_tabu[5] == l and marca_tabu[6] == l))

def texto_vitoria(v):
    arial= pygame.font.SysFont('arial', 70)
    mensagem = 'Jogador {} Venceu'.format(v)
    
    if v =='Empate':
        mens_vitoria = arial.render('DEU VELHA', True, rosa, 0)
        tela.blit(mens_vitoria, (115, 265))
    else:
        mens_vitoria = arial.render(mensagem, True, verde, 0)
        tela.blit(mens_vitoria, (0, 265))

while not terminou:
    mouse_pos = pygame.mouse.get_pos()
    if estado == 'jogando':
        desenhar_tabu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if vez == 'jogador1':
                escolha = 'X'
                testa_pos()
            else:
                escolha = 'O'
                testa_pos()
                
    if teste_vitoria('X'):
         print('X Venceu')
         texto_vitoria('X')
    
    elif teste_vitoria('O'):
         print('O Venceu')
         texto_vitoria('O')
    
    elif espaco >= 9:
         print('Empate')
         texto_vitoria('Empate')
                    

    desenhar_tabu()

    pygame.display.update()

pygame.display.quit()

pygame.quit()
