import pygame
from pygame.locals import *

pygame.init()

#posições iniciais
UP=0
DOWN=1
RIGTH=2
LEFT=3

window= pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo Da Cobrinha")

cobra= [(200,200),(210,200),(220,200)]
#declarando a possição da cobrinha
cobra_skin= pygame.surface((10,10))
cobra_skin.fill((255,255,255))# cor da cobra = branca
direção= LEFT

while True:
    for event in pygame.event.get():
        if event.type() == QUIT:
            pygame.quit()
    window.fill((0,0,0)) #para limpar a tela
    for posicao in cobra:
        window.blit(cobra_skin,posicao)

    pygame.display.update()
