import pygame
from pygame.locals import *
import random

pygame.init()

#posições iniciais
UP=0
DOWN=1
RIGHT=2
LEFT=3

WIDTH = 600
HEIGHT = 600
MACA_WIDTH = 20
MACA_HEIGHT = 20
window= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jogo Da Cobrinha")

cobra= [(200,200),(210,200),(220,200)]
#declarando a possição da cobrinha
cobra_skin= pygame.Surface((10,10))
cobra_skin.fill((255,255,255))# cor da cobra = branca
direcao= LEFT

clock = pygame.time.Clock()

background = pygame.image.load('grama.png').convert()
maca_img = pygame.image.load('maça_png-removebg-preview.png').convert_alpha()
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
LPS = 10
while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
        
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direcao = UP
            if event.key == K_DOWN:
                direcao = DOWN
            if event.key == K_LEFT:
                direcao = LEFT
            if event.key == K_RIGHT:
                direcao = RIGHT

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])

    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])

    window.fill((0,0,0)) #para limpar a tela
    for posicao in cobra:
        window.blit(cobra_skin,posicao)

    window.blit(background, (0, 0))
    window.blit(maca_img_small,maca.rect)

    pygame.display.update()
