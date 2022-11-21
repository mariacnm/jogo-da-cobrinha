import pygame
from pygame.locals import *
import random

pygame.init()

#posições iniciais
UP=0
DOWN=1
RIGTH=2
LEFT=3

WIDTH = 600
HEIGHT = 600
MACA_WIDTH = 10
MACA_HEIGHT = 10
window= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jogo Da Cobrinha")

cobra= [(200,200),(210,200),(220,200)]
#declarando a possição da cobrinha
cobra_skin= pygame.Surface((10,10))
cobra_skin.fill((255,255,255))# cor da cobra = branca
direção= LEFT

background = pygame.image.load('grama.png').convert()
maca_img = pygame.image.load('maça_png-removebg-preview.png').convert_alpha()
maca_img_small = pygame.transform.scale(maca_img, (MACA_WIDTH, MACA_HEIGHT))

class Maca(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-MACA_WIDTH)
        self.rect.y = random.randint(0, HEIGHT-MACA_HEIGHT)
        self.speedx = 0
        self.speedy = 0

maca = Maca(maca_img_small)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    window.fill((0,0,0)) #para limpar a tela
    for posicao in cobra:
        window.blit(cobra_skin,posicao)
    
    window.blit(maca_img_small,maca.rect)

    pygame.display.update()
