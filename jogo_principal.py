import pygame
from pygame.locals import *
import random

pygame.init()




def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])
    #return (c1[0]>c2[0]-10) and (c1[0]<c2[0]+10) and (c1[1]>c2[1]-10) and (c1[1]<c2[1]+10)


#posições iniciais
UP=0
DOWN=1
RIGHT=2
LEFT=3

WIDTH = 600
HEIGHT = 600
MACA_WIDTH = 25
MACA_HEIGHT = 25
window= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Jogo Da Cobrinha")

cobra= [(200,200),(210,200),(220,200)]
#declarando a possição da cobrinha
cobra_skin= pygame.Surface((10,10))
cobra_skin.fill((0,0,0))# cor da cobra = preto
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
        self.rect.x = random.randint(0, WIDTH-MACA_WIDTH)//10*10
        self.rect.y = random.randint(0, HEIGHT-MACA_HEIGHT)//10*10
        self.speedx = 0
        self.speedy = 0

maca = Maca(maca_img_small)
LPS = 10
while True:
    window.blit(background, (0, 0))
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
                

    if collision(cobra[0], maca.rect):
        print('bateu')
        maca.rect.x = random.randint(0, WIDTH-MACA_WIDTH)//10*10
        maca.rect.y = random.randint(0, HEIGHT-MACA_HEIGHT)//10*10
        print('bateu')
        cobra.append((0,0))

    
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
    window.blit(background, (0, 0))


    for posicao in cobra:
        window.blit(cobra_skin,posicao)

<<<<<<< HEAD
   

=======
    #window.blit(background, (0, 0))
>>>>>>> d6c04f1c1bbb9e6c845fe4f00049e39d2d4602b9
    window.blit(maca_img_small,maca.rect)







    pygame.display.update()
