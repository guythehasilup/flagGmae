import pygame
import game_field
import consts
import soldier
import random
import guard
from time import time

import teleport

screen_1 = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
guard.start_time = time()


def draw_game(state):
    screen_1.fill(consts.BACKGROUND_COLOR)
    soldier_pos = soldier.get_soldier_pos(game_field.game_field_metrics)
    guard_pos = guard.get_guard_pos()
    if time() - guard.start_time >= consts.GUARD_MOVEMENT_INTERVAL:
        guard.set_guard_pos(guard_pos[0] + consts.GUARD_MOVEMENT_INDEX, guard_pos[1], state)
        guard.start_time = time()
    draw_guard(guard_pos[0] * consts.SQUARE_EDGE, guard_pos[1] * consts.SQUARE_EDGE)
    draw_soldier(soldier_pos[0] * consts.SQUARE_EDGE, soldier_pos[1] * consts.SQUARE_EDGE)
    draw_flag()
    draw_bushes()
    for single_teleport in teleport.teleports:
        draw_teleport(single_teleport)
    pygame.display.flip()


def set_bush_placement():
    for bush in range(20):
        x_place = random.randint(0, consts.MATRIX_WIDTH - 2)
        y_place = random.randint(0, consts.MATRIX_HEIGHT - 2)
        consts.BUSH_PLACEMENT.append((x_place, y_place))


def draw_bushes():
    for bush_pos in consts.BUSH_PLACEMENT:
        sized_bush = pygame.transform.scale(consts.BUSH_IMAGE, (
            consts.SQUARE_EDGE * consts.BUSH_WIDTH, consts.SQUARE_EDGE * consts.BUSH_HEIGHT))
        screen_1.blit(sized_bush, (bush_pos[0] * consts.SQUARE_EDGE, bush_pos[1] * consts.SQUARE_EDGE))


def draw_night_rect(x, y):
    for i in range(4):
        pygame.draw.rect(screen_1, consts.BORDER_COLOR,
                         (x, y, consts.SQUARE_EDGE, consts.SQUARE_EDGE), 1)


def draw_night_vision_game():
    screen_1.fill(consts.NIGHT_VISION_BACKGROUND)
    y = 0
    for row in range(consts.MATRIX_HEIGHT):
        x = 0
        for col in range(consts.MATRIX_WIDTH):
            draw_night_rect(x, y)
            x += consts.SQUARE_EDGE
        y += consts.SQUARE_EDGE
    soldier_pos = soldier.get_soldier_pos(game_field.game_field_metrics)
    draw_night_soldier(soldier_pos[0] * consts.SQUARE_EDGE, soldier_pos[1] * consts.SQUARE_EDGE)
    for mine in game_field.mines:
        draw_mine(mine)
    pygame.display.flip()


def draw_soldier(x, y):
    sized_soldier = pygame.transform.scale(consts.SOLDIER_IMAGE, (
        consts.SQUARE_EDGE * consts.SOLDIER_WIDTH, consts.SQUARE_EDGE * consts.SOLDIER_HEIGHT))
    screen_1.blit(sized_soldier, (x, y))


def draw_night_soldier(x, y):
    sized_soldier = pygame.transform.scale(consts.NIGHT_SOLDIER_IMAGE, (
        consts.SQUARE_EDGE * consts.SOLDIER_WIDTH, consts.SQUARE_EDGE * consts.SOLDIER_HEIGHT))
    screen_1.blit(sized_soldier, (x, y))


def draw_flag():
    sized_flag = pygame.transform.scale(consts.FLAG_IMAGE, (
        consts.SQUARE_EDGE * consts.FLAG_WIDTH, consts.SQUARE_EDGE * consts.FLAG_HEIGHT))
    screen_1.blit(sized_flag, (consts.FLAG_X_POS * consts.SQUARE_EDGE, consts.FLAG_Y_POS * consts.SQUARE_EDGE))


def draw_mine(mine):
    sized_mine = pygame.transform.scale(consts.MINE_IMAGE, (
        consts.SQUARE_EDGE * consts.MINE_WIDTH, consts.SQUARE_EDGE * consts.MINE_HEIGHT))
    screen_1.blit(sized_mine, (mine[0][1] * consts.SQUARE_EDGE, mine[0][0] * consts.SQUARE_EDGE))


def draw_lose_screen():
    font = pygame.font.SysFont(consts.FONT_NAME, consts.MESSAGE_FONT)
    text_img = font.render(consts.LOSE_MESSAGE, True, consts.MESSAGE_COLOR)
    screen_1.blit(text_img, consts.MESSAGE_PLACE)


def draw_teleport(single_teleport):
    sized_teleport = pygame.transform.scale(consts.TELEPORT_IMAGE, (
        consts.SQUARE_EDGE * consts.TELEPORT_WIDTH, consts.SQUARE_EDGE * consts.TELEPORT_HEIGHT))
    screen_1.blit(sized_teleport,
                  (single_teleport[0][1] * consts.SQUARE_EDGE, single_teleport[0][0] * consts.SQUARE_EDGE))


def draw_win_screen():
    font = pygame.font.SysFont(consts.FONT_NAME, consts.MESSAGE_FONT)
    text_img = font.render(consts.WIN_MESSAGE, True, consts.MESSAGE_COLOR)
    screen_1.blit(text_img, consts.MESSAGE_PLACE)


def draw_explosion(x, y):
    sized_exp = pygame.transform.scale(consts.EXPLOSION_IMAGE, (
        consts.SQUARE_EDGE * consts.EXPLOSION_WIDTH, consts.SQUARE_EDGE * consts.EXPLOSION_HEIGHT))
    screen_1.blit(sized_exp, (x, y))


def draw_guard(x, y):
    sized_guard = pygame.transform.scale(consts.GUARD_IMAGE, (
        consts.SQUARE_EDGE * consts.GUARD_WIDTH, consts.SQUARE_EDGE * consts.GUARD_HEIGHT))
    rotated_guard = pygame.transform.rotate(sized_guard, consts.GUARD_ROTATION_DEGREE)
    consts.GUARD_ROTATION_DEGREE += 1
    screen_1.blit(rotated_guard, (x, y))
