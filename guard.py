import game_field
import consts
import soldier

start_time = 0
guard_index = []


def get_guard_pos():
    for col in range(len(game_field.game_field_metrics[consts.GUARDING_ROW])):
        if game_field.game_field_metrics[consts.GUARDING_ROW][col] == consts.GUARD_PLACEMENT:
            return col, consts.GUARDING_ROW


def set_guard_pos(x_pos, y_pos, state):
    remove_guard_from_row(game_field.game_field_metrics)
    for row in range(consts.GUARD_HEIGHT):
        for col in range(consts.GUARD_WIDTH):
            if x_pos + col >= consts.MATRIX_WIDTH:
                consts.GUARD_MOVEMENT_INDEX = -1
            elif x_pos + col < 0:
                consts.GUARD_MOVEMENT_INDEX = 1
            else:
                if soldier.is_touching_guard(soldier.get_soldier_pos(game_field.game_field_metrics)):
                    soldier.loss(state, soldier.soldier_feet(game_field.game_field_metrics))
                guard_index[row][col] = [row + y_pos, col + x_pos]
                game_field.game_field_metrics[row + y_pos][col + x_pos] = consts.GUARD_PLACEMENT


def remove_guard_from_row(game_field_metrics):
    for row in range(consts.GUARDING_ROW, consts.GUARDING_ROW + 2):
        for col in range(len(game_field_metrics[consts.GUARDING_ROW])):
            if game_field_metrics[row][col] == consts.GUARD_PLACEMENT:
                game_field_metrics[row][col] = consts.EMPTY_PLACEMENT
