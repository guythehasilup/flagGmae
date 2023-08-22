import consts
import random

game_field_metrics = []
mines = []


def initiate_empty_game_field():
    for row in range(consts.MATRIX_HEIGHT):
        curr_row = []
        for col in range(consts.MATRIX_WIDTH):
            curr_row.append(consts.EMPTY_PLACEMENT)
        game_field_metrics.append(curr_row)


def initiate_game_field():
    initiate_soldier_pos()
    initiate_flag_pos()
    initiate_mines_pos()


def print_board():
    for row in range(consts.MATRIX_HEIGHT):
        print()
        print(game_field_metrics[row])


def initiate_soldier_pos():
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            game_field_metrics[row][col] = consts.SOLDIER_PLACEMENT


def initiate_flag_pos():
    for row in range(consts.MATRIX_HEIGHT - consts.FLAG_HEIGHT, consts.MATRIX_HEIGHT):
        for col in range(consts.MATRIX_WIDTH - consts.FLAG_WIDTH, consts.MATRIX_WIDTH):
            game_field_metrics[row][col] = consts.FLAG_PLACEMENT


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
    for i in range(20):
        mine_row = random.randint(0, consts.MATRIX_HEIGHT - 1)
        mine_start_col = random.randint(0, consts.MATRIX_WIDTH)
        while not check_placement_of_mine(mine_row, mine_start_col):
            mine_row = random.randint(0, consts.MATRIX_HEIGHT - 1)
            mine_start_col = random.randint(0, consts.MATRIX_WIDTH)
        insert_mine_to_matrix(mine_row, mine_start_col)


def get_flag_pos():
    for row in range(consts.MATRIX_HEIGHT):
        for col in range(consts.MATRIX_WIDTH):
            if game_field_metrics[row][col] == consts.FLAG_PLACEMENT:
                return row, col
