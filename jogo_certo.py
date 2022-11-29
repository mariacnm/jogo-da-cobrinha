import pygame
from pygame.locals import *
import random

WINDOW_SIZE = (600, 600)
PIXEL_SIZE = 10


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


def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()

