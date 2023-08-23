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
# colors
BACKGROUND_COLOR = (0, 100, 0)
NIGHT_VISION_BACKGROUND = (0, 0, 0)
BORDER_COLOR = (0, 100, 0)

WINDOW_WIDTH = MATRIX_WIDTH * SQUARE_EDGE
WINDOW_HEIGHT = MATRIX_HEIGHT * SQUARE_EDGE

RUNNING_STATE = 1
ENG_GAME_STATE = 0

WIN_MESSAGE = "You Won !!!"
LOSE_MESSAGE = "You Lost !!!"
FONT_NAME = "Calibri"
MESSAGE_FONT = int(0.05 * WINDOW_WIDTH)
MESSAGE_COLOR = (0, 0, 0)
MESSAGE_PLACE = \
    (0.2 * WINDOW_WIDTH, WINDOW_HEIGHT / 2 - (MESSAGE_FONT / 2))
