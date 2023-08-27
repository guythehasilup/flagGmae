import consts
import random

import guard
import teleport

game_field_metrics = []
mines = []
flag = []


def initiate_empty_game_field():
    for row in range(consts.MATRIX_HEIGHT):
        curr_row = []
        for col in range(consts.MATRIX_WIDTH):
            curr_row.append(consts.EMPTY_PLACEMENT)
        game_field_metrics.append(curr_row)


def initiate_game_field():
    initiate_soldier_pos()
    initiate_guard_pos()
    initiate_flag_pos()
    initiate_mines_pos()
    teleport.initiate_teleport_pos()


def print_board():
    for row in range(consts.MATRIX_HEIGHT):
        print()
        print(game_field_metrics[row])


def initiate_soldier_pos():
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            game_field_metrics[row][col] = consts.SOLDIER_PLACEMENT


def initiate_guard_pos():
    for row in range(consts.GUARD_HEIGHT):
        curr_row = []
        for col in range(consts.GUARD_WIDTH):
            curr_row.append([row + consts.GUARDING_ROW, col])
            game_field_metrics[row + consts.GUARDING_ROW][col] = consts.GUARD_PLACEMENT
        guard.guard_index.append(curr_row)


def set_soldier_pos(soldier_pos):
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            game_field_metrics[row + soldier_pos[1]][col + soldier_pos[0]] = consts.SOLDIER_PLACEMENT


def clear_soldier_pos(soldier_pos):
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            game_field_metrics[row + soldier_pos[1]][col + soldier_pos[0]] = consts.EMPTY_PLACEMENT


def initiate_flag_pos():
    flag_placement = []
    for row in range(consts.MATRIX_HEIGHT - consts.FLAG_HEIGHT, consts.MATRIX_HEIGHT):
        for col in range(consts.MATRIX_WIDTH - consts.FLAG_WIDTH, consts.MATRIX_WIDTH):
            game_field_metrics[row][col] = consts.FLAG_PLACEMENT
            flag_placement.append([row, col])
        flag.append(flag_placement)


def check_placement_of_mine(mine_row, mine_start_col):
    if mine_start_col + consts.MINE_WIDTH > consts.MATRIX_WIDTH:
        return False
    for cols in range(mine_start_col, mine_start_col + consts.MINE_WIDTH):
        if game_field_metrics[mine_row][cols] != consts.EMPTY_PLACEMENT:
            return False
    return True


def insert_mine_to_matrix(mine_row, mine_start_col):
    mine_placement = []
    for cols in range(mine_start_col, mine_start_col + consts.MINE_WIDTH):
        game_field_metrics[mine_row][cols] = consts.MINE_PLACEMENT
        mine_placement.append((mine_row, cols))
    mines.append(mine_placement)


def initiate_mines_pos():
    for i in range(consts.MINE_NUMBER):
        mine_row = random.randint(0, consts.MATRIX_HEIGHT - 1)
        mine_start_col = random.randint(0, consts.MATRIX_WIDTH)
        while not check_placement_of_mine(mine_row, mine_start_col):
            mine_row = random.randint(0, consts.MATRIX_HEIGHT - 1)
            mine_start_col = random.randint(0, consts.MATRIX_WIDTH)
        insert_mine_to_matrix(mine_row, mine_start_col)


def set_mines_pos(mine_list):
    for mine in mine_list:
        insert_mine_to_matrix(mine[0][0], mine[0][1])


def restore_mines():
    for mine in mines:
        for parts_of_mine in mine:
            if game_field_metrics[parts_of_mine[0]][parts_of_mine[1]] == consts.EMPTY_PLACEMENT:
                game_field_metrics[parts_of_mine[0]][parts_of_mine[1]] = consts.MINE_PLACEMENT


def clear_board():
    for row in range(consts.MATRIX_HEIGHT):
        for col in range(consts.MATRIX_WIDTH):
            if game_field_metrics[row][col] in [consts.SOLDIER_PLACEMENT, consts.MINE_PLACEMENT]:
                game_field_metrics[row][col] = consts.EMPTY_PLACEMENT
