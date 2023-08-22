import pygame

import consts

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_game():
    screen.fill(consts.BACKGROUND_COLOR)
    draw_soldier(0,0)
    pygame.display.flip()


def draw_night_rect(x, y):
    for i in range(4):
        pygame.draw.rect(screen, consts.BORDER_COLOR,
                         (x, y, consts.SQUARE_EDGE, consts.SQUARE_EDGE), 1)


def draw_night_vision_game():
    y = 0
    for row in range(consts.MATRIX_HEIGHT):
        x = 0
        for col in range(consts.MATRIX_WIDTH):
            draw_night_rect(x, y)
            x += consts.SQUARE_EDGE
        y += consts.SQUARE_EDGE
    draw_night_soldier(0,0)
    pygame.display.flip()


def draw_soldier(x, y):
    sized_soldier = pygame.transform.scale(consts.SOLDIER_IMAGE, (
        consts.SQUARE_EDGE * consts.SOLDIER_WIDTH, consts.SQUARE_EDGE * consts.SOLDIER_HEIGHT))
    screen.blit(sized_soldier, (x, y))


def draw_night_soldier(x, y):
    sized_soldier = pygame.transform.scale(consts.NIGHT_SOLDIER_IMAGE, (
        consts.SQUARE_EDGE * consts.SOLDIER_WIDTH, consts.SQUARE_EDGE * consts.SOLDIER_HEIGHT))
    screen.blit(sized_soldier, (x, y))


def draw_flag():
    pass
