# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()
pygame.mixer.init()

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
    assets['cabeça.png'] = pygame.image.load('assets/cabeça.png').convert_alpha()
    assets['cabeça.png'] = pygame.transform.scale(assets['cabeça.png'], (COBRA_WIDTH, COBRA_HEIGHT))
    assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    pygame.mixer.music.set_volume(0.4)
    assets['boom_sound'] = pygame.mixer.Sound('assets/snd/expl3.wav')
    assets['destroy_sound'] = pygame.mixer.Sound('assets/snd/expl6.wav')
    assets['pew_sound'] = pygame.mixer.Sound('assets/snd/pew.wav')
    return assets