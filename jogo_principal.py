import pygame
from pygame.locals import *

pygame.init()

window= pygame.display.set_mode((600,600))
pygame.display.set_caption("Jogo Da Cobrinha")

while True:
    for event in pygame.event.get():
        if event.type() == QUIT:
            pygame.quit()

    pygame.display.update()
