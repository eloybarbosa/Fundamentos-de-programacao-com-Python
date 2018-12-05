import pygame

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

pygame.init()
tela = pygame.display.set_mode((600, 600))
fonte = pygame.font.SysFont('Calibri', 50)
terminou = False

clock = pygame.time.Clock()


tabuleiro = [
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







while not terminou:
    mouse_pos = pygame.mouse.get_pos()
# Checar os eventos do mouse aqui:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_pos)
# Fazemos a atualização aqui!

# Atualiza o desenho na tela
pygame.display.update()
# Configura 50 atualizações de tela por segundo
clock.tick(50)
# Finaliza a janela do jogo
pygame.display.quit()
# Finaliza o pygame
pygame.quit()
