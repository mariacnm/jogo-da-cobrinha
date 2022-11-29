import pygame
from pygame.locals import *
import random

pygame.init()
pygame.mixer.init()

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10

pygame.mixer.music.load('assets.py/musica_principal.mp3')
pygame.mixer.music.set_volume(0.4)
mordendo_sound = pygame.mixer.Sound('assets.py/mordendo.mp3')


def collision(pos1, pos2):
    return pos1 == pos2


def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True


def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

snake_pos = [(250, 50), (260, 50), (270, 50)]
snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_surface.fill((255, 255, 255))
snake_direction = K_LEFT

apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple_surface.fill((255, 0, 0))
apple_pos = random_on_grid()


'''def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()'''
score=0
pygame.mixer.music.play(loops=-1)
while True:
    pygame.time.Clock().tick(15)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()
        elif event.type == KEYDOWN:
            if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                snake_direction = event.key

    screen.blit(apple_surface, apple_pos)

    if collision(apple_pos, snake_pos[0]):

        snake_pos.append((-10, -10))
        apple_pos = random_on_grid()
        score+=10
        print(score)

    for pos in snake_pos:
        screen.blit(snake_surface, pos)

    for i in range(len(snake_pos) - 1, 0, -1):
        if collision(snake_pos[0], snake_pos[i]):
            #restart_game()
            pygame.quit()
            quit()
            break
        snake_pos[i] = snake_pos[i - 1]

    if off_limits(snake_pos[0]):
       
       pygame.quit()
       quit()

    if snake_direction == K_UP:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_DOWN:
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_LEFT:
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_RIGHT:
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()