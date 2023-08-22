import pygame

import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()


def draw_night_rect(x, y):
    for i in range(4):
        pygame.draw.rect(screen, consts.BORDER_COLOR,
                         (x, y, consts.SQUARE_EDGE, consts.SQUARE_EDGE), 1)


def draw_night_vision_game():
    # pygame.draw.rect(screen, consts.NIGHT_VISION_BACKGROUND,
    # (consts.SQUARE_EDGE, consts.SQUARE_EDGE, consts.SQUARE_EDGE, consts.SQUARE_EDGE), 0)
    y = 0
    for row in range(consts.MATRIX_HEIGHT):
        x = 0
        for col in range(consts.MATRIX_WIDTH):
            draw_night_rect(x, y)
            x += consts.SQUARE_EDGE
        y += consts.SQUARE_EDGE
    pygame.display.flip()


def draw_soldier():
    pass


def draw_flag():
    pass
