#importando pygame
import pygame
from pygame.locals import *
import random

#cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
VERDE = (133, 187, 101)

lista_cor=[WHITE,RED,GREEN,BLUE,YELLOW]
#importando py music
pygame.init()
pygame.mixer.init()

#janela do jogo
WINDOW_SIZE = (600, 600) #pixel
PIXEL_SIZE = 10
INIT = 0
GAME = 1
QUIT = 2
errou=3

M_principal=pygame.mixer.music.load('assets.py/sons/musica_principal2.mp3') #musica principal(mario bros)
M_principal=pygame.mixer.music.set_volume(0.4)#volume da musica principal
mordendo_sound = pygame.mixer.Sound('assets.py/sons/mordendo.mp3')#musica quando morde a maça
fail_sound = pygame.mixer.Sound('assets.py/sons/fail.mp3')#musica de game over

#tentamos fazer uma classe para a maca mais nao deu certo
#class Maca(pygame.sprite.Sprite):
    #def __init__(self, img):
        # Construtor da classe mãe (Sprite).
       # pygame.sprite.Sprite.__init__(self)

       # self.image = img
       # self.rect = self.image.get_rect()
       # self.rect.x = random.randint(0, WIDTH-MACA_WIDTH)//10*10
       # self.rect.y = random.randint(0, HEIGHT-MACA_HEIGHT)//10*10
       # self.speedx = 0
       # self.speedy = 0


#funcao para tela inicial
def tela_inicial(screen):
    background= pygame.image.load("assets.py/imagens/jogo.png").convert()
    background_rect= background.get_rect()
    rodando=True
    while rodando:
        pygame.time.Clock().tick(15)
        screen.fill((0, 0, 0))
        screen.blit(background,background_rect)
        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                rodando = False
                return QUIT
            if event.type == pygame.KEYUP:
                state = GAME
                print('GAME')
                return GAME

        pygame.display.flip()







#funcao de colissão
def collision(pos1, pos2):
    state= errou
    return pos1 == pos2

#funcao de limite de tela bateu morreu
def off_limits(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        state=errou
        return False
    else:
        return True

def tela_gameover(screen):
    fundo_over= pygame.image.load("assets.py/imagens/gameover.png").convert()
    fundo_over_rect= fundo_over.get_rect()
    rodando2=True
    while rodando2:
        pygame.time.Clock().tick(12)
        screen.fill((0, 0, 0))
        screen.blit(fundo_over,fundo_over_rect)
        
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                rodando2 = False
                return QUIT
            if collision and off_limits:
                state = errou
                return errou

        pygame.display.flip()
        
#funcao para criar maças aleatorias
def random_on_grid():
    x = random.randint(0, WINDOW_SIZE[0])
    y = random.randint(0, WINDOW_SIZE[1])
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE

font_name = pygame.font.match_font("comicsansms")
#funcao para aparecer pontuação
def mensagem_tela(message, color, font_size, x, y):
    font = pygame.font.SysFont(font_name, font_size)
    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x,y)
    return screen.blit(text, text_rect)


pygame.init()
#tela 
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Snake')

def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_LEFT
    apple_pos = random_on_grid()


def jogo(screen):

    score=0
    M_principal=pygame.mixer.music.play(loops=-1)
    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
    snake_surface.fill((255, 255, 255))
    snake_direction = K_LEFT

    apple_surface = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
    apple_surface.fill((255, 0, 0))
    apple_pos = random_on_grid()
    
    fps=12
    soma = 0
    while True:
        pygame.time.Clock().tick(fps)
        screen.fill((133, 187, 101))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
                
            elif event.type == KEYDOWN:
                if event.key in [K_UP, K_DOWN, K_LEFT, K_RIGHT]:
                    snake_direction = event.key


        screen.blit(apple_surface, apple_pos)



        if collision(apple_pos, snake_pos[0]):#colisao com a maça
            mordendo_sound.play()
            snake_pos.append((-20, -20))
            apple_pos = random_on_grid()
            score+=10
            if score >=50:
                snake_surface.fill((255, 255, 0))
            if score >=100:
                snake_surface.fill((0, 71, 170))
                fps=15
            if score >=150:
                snake_surface.fill((0, 102, 51))
            if score >= 200:
                snake_surface.fill((148, 0, 211))
                fps=18
            if score >= 250:
                snake_surface.fill((0, 255, 255))
            if score >= 300:
                snake_surface.fill((0, 0, 0))
                fps=22
            if score>= 350:
                snake_surface.fill((255,140,0))
            if score>= 400:
                snake_surface.fill((128,0,0))
            if score>= 450:
                snake_surface.fill((102,51,51))
            if score>= 500:
                snake_surface.fill((148,0,211))
                fps=25

        printa = mensagem_tela("Score: " + str(score), WHITE, 24, 600/2, 10) #score
        for pos in snake_pos:
            screen.blit(snake_surface, pos)
        
        for i in range(len(snake_pos) - 1, 0, -1): #colisao com a propria cobra
            if collision(snake_pos[0], snake_pos[i]):
                state=errou
                M_principal=pygame.mixer.music.pause()
                #tentamos colocar uma musica quanodo da gameover mas não deu certo achamos que e o tamanho da musica
                #fail_sound=pygame.mixer.music.play(loops=-1)
                if state == errou:
                    fundo_over= pygame.image.load("assets.py/imagens/gameover.png").convert()
                    fundo_over_rect= fundo_over.get_rect()
                    screen.fill((0,0,0))
                    screen.blit(fundo_over,fundo_over_rect)
                    printa = mensagem_tela("Score: " + str(score), WHITE, 50, 600/2, 25) #score
                False
                #pygame.quit()
                #quit()
            snake_pos[i] = snake_pos[i - 1]

        if off_limits(snake_pos[0]):
            state=errou
            M_principal=pygame.mixer.music.pause()
            #tentamos colocar uma musica quanodo da gameover mas não deu certo achamos que e o tamanho da musica
            #fail_sound=pygame.mixer.music.play(loops=-1)
            if state==errou :
                fundo_over= pygame.image.load("assets.py/imagens/gameover.png").convert()
                fundo_over_rect= fundo_over.get_rect()
                screen.fill((0,0,0))
                screen.blit(fundo_over,fundo_over_rect)
                printa = mensagem_tela("Score: " + str(score), WHITE, 50, 600/2, 25) #score
            False
           #pygame.quit()
            #quit()

        if snake_direction == K_UP:
            snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
        elif snake_direction == K_DOWN:
            snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
        elif snake_direction == K_LEFT:
            snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
        elif snake_direction == K_RIGHT:
            snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])
        pygame.display.update()



state = INIT
while state!=QUIT:
    if state == INIT:
        state = tela_inicial(screen)
    elif state == GAME:
        state = jogo(screen)
    elif state== errou:
        state= tela_gameover(screen)
    else:
        state= QUIT


