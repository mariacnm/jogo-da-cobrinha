# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
#pygame.mixer.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Jogo da Cobrinha')

# ----- Inicia assets
FPS = 10
COBRA_WIDTH = 10
COBRA_HEIGHT = 10
MACA_WIDTH = 10
MACA_HEIGHT = 10

def load_assets():
    assets = {}
    assets['cabeça_png'] = pygame.image.load('assets/cabeça.png').convert_alpha()
    assets['cabeça_png'] = pygame.transform.scale(assets['cabeça.png'], (COBRA_WIDTH, COBRA_HEIGHT))
    assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

    # Carrega os sons do jogo
    #pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    #pygame.mixer.music.set_volume(0.4)
    #assets['mordendo_sound'] = pygame.mixer.Sound('assets/snd/expl3.wav')
    #assets['musiquinha_sound'] = pygame.mixer.Sound('assets/snd/pew.wav')
    return assets

class Corpo(pygame.sprite.Sprite):
    def _init_(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite._init_(self)

        self.lista = [(200,200),(210,200),(220,200)]
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 5
        self.speedy = 0
        self.groups = groups
        self.assets = assets

    def update(self):
            # Atualização da posição da nave
            self.rect.x += self.speedx
            

class Cabeca(pygame.sprite.Sprite):
    def _init_(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite._init_(self)

        self.lista = []
        self.image = assets['cabeça_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 2
        self.speedx = 5
        self.speedy = 0
        self.groups = groups
        self.assets = assets


    def update(self):
            # Atualização da posição da nave
            self.rect.x += self.speedx

            # Mantem dentro da tela
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0
