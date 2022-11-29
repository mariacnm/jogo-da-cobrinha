import pygame
from pygame.locals import *
import random

pygame.init()

def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return (x//10 * 10, y//10 * 10)

def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
window = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

cobra = [(200, 200), (210, 200), (220,200)]
cobra_skin = pygame.Surface((10,10))
cobra_skin.fill((255,255,255))

apple_pos = []

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
        #if collision (cobra[0] in cobra):
            #while False
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

    for apple_pos_u in apple_pos:
        window.blit(apple, apple_pos_u)
    for pos in cobra:
        window.blit(cobra_skin,pos)

    pygame.display.update()