import pygame
import os

# Inicializa o pygame (opcional aqui; mantive para compatibilidade)
pygame.init()

# Diretório base do projeto (garante caminhos estáveis)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ========================= ECRÃ =========================
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h

# ========================= CORES =========================
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
RED = (220, 50, 50)
RED_HOVER = (200, 30, 30)
PRIMARY = (40, 120, 220)
PRIMARY_HOVER = (30, 100, 200)

# ========================= FPS =========================
FPS = 60

# ========================= ASSETS =========================
ASSET_DIR = BASE_DIR
IMAGES_DIR = os.path.join(ASSET_DIR, "Imagens_usadas")

HIGHSCORE_FILE = os.path.join(BASE_DIR, "highscore.json")
PROGRESS_FILE = os.path.join(BASE_DIR, "progress.json")

# ========================= CHÃO =========================
MANUAL_GROUND_Y = 780
GROUND_Y = int(HEIGHT * 0.8)  # será atualizado por main quando o bg for carregado

# ========================= SIZES =========================
PLAYER_SIZE_NORMAL = (140, 140)
PLAYER_SIZE_SHOOT = (150, 150)
FIREBALL_SIZE = (64, 64)
BOSS_BULLET_SIZE = (98, 98)
POWERUP_SIZE = (110, 110)

# ========================= BOSS =========================
BOSS_HITBOX_INSET = (140, 120)
BOSS_HITBOX_OFFSET = (-28, 0)

# ========================= TRONCOS =========================
CACTUS_SCALE_MIN = 0.75
CACTUS_SCALE_MAX = 1.25
CACTUS_MIN_WIDTH = 60
CACTUS_MAX_WIDTH = 160
CACTUS_MIN_HEIGHT = 60
CACTUS_MAX_HEIGHT = min(int(PLAYER_SIZE_NORMAL[1] * 1.05), int(HEIGHT * 0.33))

# ========================= NÍVEIS =========================
LEVEL_DISTANCES = {
    1: 1000,
    2: 2000,
    3: 3000,
    4: 4200,
    5: float("inf"),
}

# ========================= FONTES =========================
TITLE_FONT = pygame.font.SysFont("Arial", 60, bold=True)
TITLE_FONT_MENU = pygame.font.SysFont("Comic Sans MS", 70, bold=True)
BTN_FONT = pygame.font.SysFont("Arial", 32)
HUD_FONT = pygame.font.SysFont("Arial", 30)

# ========================= ESTADO GLOBAL =========================
# unlocked_levels será carregado no startup pelo main (via funcionalidades.load_progress)
unlocked_levels = 1