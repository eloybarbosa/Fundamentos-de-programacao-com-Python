#17. Usando a biblioteca Pygame, escreva um programa que implemente o jogo “Pong” (visto no curso), com uma modificação. Tal modificação consiste em incluir o aumento da velocidade da bola. O aumento será feito de maneira gradual, isto é, cada 10 vezes que a bola bater na paleta do jogador1 a velocidade aumenta em 1. (código e printscreen)

import pygame, sys
from pygame.locals import *

# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 400
ALTURA_TELA = 300
# Valores para o desenho das paletas e do fundo
LARGURA_LINHA = 10
PALETA_TAMANHO = 50
PALETAOFFSET = 20
# Cores
PRETO 	= (0, 0, 0)
BRANCO = (255,255,255)
#VARIAVEIS
# Será utilizado para a velocidade do jogo
fps = 250
colisao1=0
loop=0
      
# Função para desenhar a arena
def desenhaArena():
    TELA.fill(BRANCO)
    # Desenha a quadra
    pygame.draw.rect(TELA, PRETO, ((0,0), (LARGURA_TELA,ALTURA_TELA)), LARGURA_LINHA*2)
    # Desenha a linha no centro
    pygame.draw.line(TELA, PRETO, ((LARGURA_TELA//2),0), ((LARGURA_TELA//2),ALTURA_TELA), (LARGURA_LINHA//4))
    
# Função para desenhar a paleta
def desenhaPaleta(paleta):
    #Impede da paleta ir  além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    #Impede da paleta ir  além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
        #Desenha a paleta
    pygame.draw.rect(TELA, PRETO, paleta)
        
        
# Função para desenhar a bola
def desenhaBola(bola):
    pygame.draw.rect(TELA, PRETO, bola)
    
#altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
        bola.x += bolaDirX
        bola.y += bolaDirY
        return bola
    
# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verificaColisao(bola, bolaDirX, bolaDirY):
    if bola.top == (LARGURA_LINHA) or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
            bolaDirY = bolaDirY * -1
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA):
            bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY

# Rotina de IA para o NPC.
def inteligenciaArtificial(bola, bolaDirX, paleta2):
# Movimentar a paleta quando a bola vem em direção da paleta
    if bolaDirX == 1:
            if paleta2.centery < bola.centery:
                paleta2.y += 1
            else:
                paleta2.y -=1
    return paleta2

#Verifica a colisão da bola com a paleta1 ou paleta2    
def verificaColisaoBola(bola, paleta1, paleta2, bolaDirX):
        
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        return -1
    
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        return -1
    else:
        return 1
    

#Verifica se o jogador fez ponto e retorna o novo valor do placar
def verificaPlacar(paleta1, bola, placar, bolaDirX):
    #zera a contagem se a bola acerta a borda do jogador
    if bola.left == LARGURA_LINHA: 
        return 0
    #1 ponto por acertar a bola
    elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 1
        return placar
    #10 pontos se vender a paleta do computador
    elif bola.right == LARGURA_TELA - LARGURA_LINHA:
        placar += 10
        return placar
    #retorna o mesmo placar se nenhum ponto foi adicionado
    else: return placar
    
def verificacolisao(paleta1, bola, colisao1, bolaDirX):
   
    if bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        colisao1 += 1
        return colisao1
    else: return colisao1
    
  

def desenhaPlacar(placar):
    resultadoSurf = BASICFONT.render('placar = %s' %(placar), True, PRETO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 150, 25)
    TELA.blit(resultadoSurf, resultadoRect)
    
def desenhaColisoes(colisao):
    resultadoSurf = BASICFONT.render('Colisão = %s' %(colisao), True, PRETO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 350, 25)
    TELA.blit(resultadoSurf, resultadoRect)
    
def desenhavelocidade(fps):
    resultadoSurf = BASICFONT.render('Velocidade = %s' %(fps), True, PRETO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 380, 265)
    TELA.blit(resultadoSurf, resultadoRect)
    
    
    
#funcao Principal
def main():
    pygame.init()  
        
    #Informação da fonte
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)

    global TELA

    FPSCLOCK = pygame.time.Clock()
    TELA = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption('PongNet')
    colisao10=False
    
    #Iniciando as variáveis nas posições iniciais
    #Estas variáveis serão alteradas ao longo da execução
    bolaX = LARGURA_TELA//2 - LARGURA_LINHA//2
    bolaY = ALTURA_TELA//2 - LARGURA_LINHA//2
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2
    placar = 0
    colisao1 = 0
    fps = 250
    
   
    #altera a posição da bola
    bolaDirX = -1
    bolaDirY = -1

    #Criando os retangulos para a bola e paletas.
    paleta1 = pygame.Rect(PALETAOFFSET,jogadorUm_posicao,LARGURA_LINHA,PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)

    #Desenhando as posições iniciais da Arena
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)

    pygame.mouse.set_visible(0)
    
    while True: #Loop principal
        for event in pygame.event.get():
                if event.type == QUIT:
                   pygame.quit()
                   sys.exit()
                elif event.type == MOUSEMOTION:
                    mouseX, mouseY = event.pos
                    paleta1.y = mouseY            
        
        if colisao1 == 3:
            colisao10=True
            
        
        if colisao10 == True:
            fps+=10
            colisao10=False
            colisao1=0
        
        desenhaArena()
        desenhaPaleta(paleta1)
        desenhaPaleta(paleta2)
        desenhaBola(bola)
        
    
        bola = moveBola(bola, bolaDirX, bolaDirY)
        bolaDirX, bolaDirY = verificaColisao(bola, bolaDirX, bolaDirY)
        bolaDirX = bolaDirX * verificaColisaoBola(bola, paleta1, paleta2, bolaDirX)
        paleta2 = inteligenciaArtificial(bola, bolaDirX, paleta2)

        placar = verificaPlacar(paleta1, bola, placar, bolaDirX)
        colisao1 = verificacolisao(paleta1, bola, colisao1, bolaDirX)
        desenhaPlacar(placar)
        desenhaColisoes(colisao1)
        desenhavelocidade(fps)
        
    
        pygame.display.update()
        FPSCLOCK.tick(fps)
        

if __name__=='__main__':
 main()
