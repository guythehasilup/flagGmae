import random
import consts
import game_field
import soldier

teleports = []


def initiate_teleport_pos():
    for i in range(consts.TELEPORT_NUMBER):
        teleport_row = random.randint(4, consts.MATRIX_HEIGHT - 5)
        teleport_start_col = random.randint(0, consts.MATRIX_WIDTH)
        while not check_placement_of_teleport(teleport_row, teleport_start_col):
            teleport_row = random.randint(4, consts.MATRIX_HEIGHT - 5)
            teleport_start_col = random.randint(0, consts.MATRIX_WIDTH)
        insert_teleport_to_matrix(teleport_row, teleport_start_col)


def reset_teleports_to_matrix(tp_list):
    for tp in tp_list:
        insert_teleport_to_matrix(tp[0][0], tp[0][1])


def insert_teleport_to_matrix(teleport_row, teleport_start_col):
    teleport_placement = []
    for cols in range(teleport_start_col, teleport_start_col + consts.TELEPORT_WIDTH):
        game_field.game_field_metrics[teleport_row][cols] = consts.TELEPORT_PLACEMENT
        teleport_placement.append((teleport_row, cols))
    teleports.append(teleport_placement)


def check_placement_of_teleport(teleport_row, teleport_start_col):
    if teleport_start_col + consts.TELEPORT_WIDTH > consts.MATRIX_WIDTH:
        return False
    if teleport_row in [11, 12, 13, 14]:
        return False
    for cols in range(teleport_start_col, teleport_start_col + consts.TELEPORT_WIDTH):
        if game_field.game_field_metrics[teleport_row][cols] != consts.EMPTY_PLACEMENT:
            return False

    return True


def choose_random_teleport(teleport_index):
    random_teleport_index = random.randint(0, consts.TELEPORT_NUMBER - 1)
    while teleport_index == random_teleport_index:
        random_teleport_index = random.randint(0, consts.TELEPORT_NUMBER - 1)
    return random_teleport_index


def check_if_teleport_activates(soldier_feet):
    for teleport_in_list in teleports:
        for teleport_cell in teleport_in_list:
            # if any of the soldier feet are in the cell that belongs to the teleport (outside of the official grid)
            if (soldier_feet[0][0] == teleport_cell[0] and soldier_feet[0][1] == teleport_cell[1]
                    or soldier_feet[1][0] == teleport_cell[0] and soldier_feet[1][1] == teleport_cell[1]):
                # index of current teleport
                teleport_index = teleports.index(teleport_in_list)
                # index of the randomized teleport
                new_teleport_index = choose_random_teleport(teleport_index)
                # index of the top left corner of the teleport, the soldier needs to teleport 1 space above it
                index = teleports[new_teleport_index][0]
                # clears the board from the current soldier, leaves space for the new soldier
                game_field.clear_soldier_pos(soldier.get_soldier_pos(game_field.game_field_metrics))
                teleport_soldier_to_index((index[0] - 4, index[1]))


def teleport_soldier_to_index(soldier_pos):
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            game_field.game_field_metrics[row + soldier_pos[0]][col + soldier_pos[1]] = consts.SOLDIER_PLACEMENT
