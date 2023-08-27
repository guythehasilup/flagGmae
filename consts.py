import pygame

MATRIX_HEIGHT = 25
MATRIX_WIDTH = 50
SQUARE_EDGE = 25
FLAG_PLACEMENT = "F"
FLAG_WIDTH = 4
FLAG_HEIGHT = 3
FLAG_IMAGE_PATH = "bin/flag.png"
FLAG_IMAGE = pygame.image.load(FLAG_IMAGE_PATH)
FLAG_X_POS = 46
FLAG_Y_POS = 22
SOLDIER_PLACEMENT = "S"
SOLDIER_WIDTH = 2
SOLDIER_HEIGHT = 4
SOLDIER_BODY = 3
SOLDIER_FEET = 1
SOLDIER_IMAGE_PATH = "bin/soldier.png"
NIGHT_SOLDIER_IMAGE_PATH = "bin/soldier_nigth.png"
INJURED_SOLDIER_IMAGE_PATH = "bin/injury.png"
INJURED_SOLDIER_IMAGE = pygame.image.load(INJURED_SOLDIER_IMAGE_PATH)
SOLDIER_IMAGE = pygame.image.load(SOLDIER_IMAGE_PATH)
NIGHT_SOLDIER_IMAGE = pygame.image.load(NIGHT_SOLDIER_IMAGE_PATH)
MINE_PLACEMENT = "M"
MINE_WIDTH = 3
MINE_HEIGHT = 1
MINE_IMAGE_PATH = "bin/mine.png"
MINE_IMAGE = pygame.image.load(MINE_IMAGE_PATH)
MINE_NUMBER = 20
EMPTY_PLACEMENT = "E"
WELCOME_MESSAGE = "Welcome to The Flag game.\nHave Fun!"
BUSH_IMAGE_PATH = "bin/grass.png"
BUSH_IMAGE = pygame.image.load(BUSH_IMAGE_PATH)
BUSH_WIDTH = 1
BUSH_HEIGHT = 2
BUSH_PLACEMENT = []
EXPLOSION_IMAGE_PATH = "bin/explotion.png"
EXPLOSION_IMAGE = pygame.image.load(EXPLOSION_IMAGE_PATH)
EXPLOSION_WIDTH = 3
EXPLOSION_HEIGHT = 2
# guard related
GUARD_IMAGE_PATH = "bin/guard_left.png"
GUARD_IMAGE = pygame.image.load(GUARD_IMAGE_PATH)
GUARDING_ROW = int(MATRIX_HEIGHT / 2)
GUARD_WIDTH = 2
GUARD_HEIGHT = 2
GUARD_ROTATION_DEGREE = 1
GUARD_MOVEMENT_INDEX = 1
GUARD_PLACEMENT = 'G'
GUARD_MOVEMENT_INTERVAL = 0.04
# teleport related
TELEPORT_PLACEMENT = "T"
TELEPORT_WIDTH = 3
TELEPORT_HEIGHT = 1
TELEPORT_IMAGE_PATH = "bin/teleport.png"
TELEPORT_IMAGE = pygame.image.load(TELEPORT_IMAGE_PATH)
TELEPORT_NUMBER = 5
# colors
BACKGROUND_COLOR = (0, 100, 0)
NIGHT_VISION_BACKGROUND = (0, 0, 0)
BORDER_COLOR = (0, 100, 0)

WINDOW_WIDTH = MATRIX_WIDTH * SQUARE_EDGE
WINDOW_HEIGHT = MATRIX_HEIGHT * SQUARE_EDGE

RUNNING_STATE = 1
ENG_GAME_STATE = 0

DATABASE_FILE = 'db.csv'
VAR_BUSH = 0
VAR_SOLDIER = 1
VAR_MINE = 2
VAR_TELEPORT = 3

LOSE_IMAGE_PATH = "bin/lose_screen.png"
LOSE_IMAGE = pygame.image.load(LOSE_IMAGE_PATH)

VICTORY_IMAGE_PATH = "bin/victory_screen.png"
VICTORY_IMAGE = pygame.image.load(VICTORY_IMAGE_PATH)