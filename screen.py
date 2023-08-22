import pygame

import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    pygame.display.flip()


def draw_night_vision_game():
    # pygame.draw.rect(screen, consts.NIGHT_VISION_BACKGROUND,
    # (consts.SQUARE_EDGE, consts.SQUARE_EDGE, consts.SQUARE_EDGE, consts.SQUARE_EDGE), 0)

    for i in range(4):
        pygame.draw.rect(screen, consts.BORDER_COLOR,
                         (consts.SQUARE_EDGE, consts.SQUARE_EDGE, consts.SQUARE_EDGE, consts.SQUARE_EDGE), 1)
    pygame.display.flip()


def draw_soldier():
    pass


def draw_flag():
    pass
