import pygame
from pygame.locals import *
import random

pygame.init()

<<<<<<< HEAD


=======
>>>>>>> d9ebb8f7598099955ab5186b3824608499e753ca
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

#def off_limits(pos):
    if 0 <= pos[0] < window[0] and 0 <= pos[1] < window[1]:
        return False
    else:
        return True

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

<<<<<<< HEAD

=======
pygame.init()
>>>>>>> d9ebb8f7598099955ab5186b3824608499e753ca
window = pygame.display.set_mode((600,600))
PIXEL_SIZE = 10
pygame.display.set_caption('Snake')




cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))

cobra_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
cobra_skin.fill((255,255,255))

apple_pos = []

class Cobra:
    def __init__(self):
        
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-METEOR_WIDTH)
            self.rect.y = random.randint(-100, -METEOR_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

for i in range(0, 5):
    apple_pos.append(on_grid_random())

apple = pygame.Surface((10,10))
apple.fill((255,0,0))

direcao = LEFT

clock = pygame.time.Clock() 

background = pygame.image.load('grama.png').convert()

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


    for apple_pos_u in apple_pos:
        if collision(cobra[0], apple_pos_u):
            apple_pos.remove(apple_pos_u)
            apple_pos.append(on_grid_random())
            cobra.append((0,0))
        
    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i-1][0], cobra[i-1][1])
    
    if off_limits(cobra[0]):
            pygame.quit
    
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

    for apple_pos_u in apple_pos:
        window.blit(apple, apple_pos_u)
    for pos in cobra:
        window.blit(cobra_skin,pos)

    pygame.display.update()


