import consts
import game_field
import main


def soldier_move_left(game_field_metrics, state):
    feet_location = soldier_feet(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    if soldier_placement[0] - 1 < 0:
        return
    elif game_field_metrics[feet_location[0][0]][feet_location[0][1] - 1] == consts.MINE_PLACEMENT:
        state["is_lost"] = True
        return
    # move soldier left
    # remove the rightest side of soldier
    # for row in range(consts.SOLDIER_HEIGHT):
    #     game_field_metrics[][] = consts.EMPTY_PLACEMENT

def soldier_move_right(game_field_metrics, state):
    feet_location = soldier_feet(game_field_metrics)

    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if col >= consts.WINDOW_WIDTH:
                return
            elif game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT:
                if (game_field_metrics[feet_location[1][0]][feet_location[1][1] + 1]) == consts.MINE_PLACEMENT:
                    state["is_lost"] = True
                    return
                else:
                    for i in range(consts.SOLDIER_HEIGHT):
                        game_field_metrics[row + i][col] = consts.EMPTY_PLACEMENT
                        game_field_metrics[row + i][col + 1] = consts.SOLDIER_PLACEMENT
                        game_field_metrics[row + i][col + 2] = consts.SOLDIER_PLACEMENT
                    return


def soldier_move_down(game_field_metrics, state):
    feet_location = soldier_feet(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    if feet_location[0][0] + 1 == consts.MATRIX_HEIGHT:
        return
    elif (game_field_metrics[feet_location[0][0] + 1][feet_location[0][1]] == consts.MINE_PLACEMENT or
          game_field_metrics[feet_location[1][0] + 1][feet_location[1][1]] == consts.MINE_PLACEMENT):
        state["is_lost"] = True
        return
    # move soldier down
    game_field_metrics[soldier_placement[1]][soldier_placement[0]] = consts.EMPTY_PLACEMENT
    game_field_metrics[soldier_placement[1]][soldier_placement[0] + 1] = consts.EMPTY_PLACEMENT
    game_field_metrics[soldier_placement[1] + consts.SOLDIER_HEIGHT][
        soldier_placement[0]] = consts.SOLDIER_PLACEMENT
    game_field_metrics[soldier_placement[1] + consts.SOLDIER_HEIGHT][
        soldier_placement[0] + 1] = consts.SOLDIER_PLACEMENT


def soldier_move_up(game_field_metrics, state):
    feet_location = soldier_feet(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    if soldier_placement[1] - 1 < 0:
        return
    elif (game_field_metrics[feet_location[0][0] - 1][feet_location[0][1]] == consts.MINE_PLACEMENT or
          game_field_metrics[feet_location[1][0] - 1][feet_location[1][1]] == consts.MINE_PLACEMENT):
        state["is_lost"] = True
        return
    # move soldier up
    # remove lower body
    game_field_metrics[soldier_placement[1] + consts.SOLDIER_BODY][soldier_placement[0]] = consts.EMPTY_PLACEMENT
    game_field_metrics[soldier_placement[1] + consts.SOLDIER_BODY][soldier_placement[0] + 1] = consts.EMPTY_PLACEMENT
    # move up
    game_field_metrics[soldier_placement[1] - 1][
        soldier_placement[0]] = consts.SOLDIER_PLACEMENT
    game_field_metrics[soldier_placement[1] - 1][
        soldier_placement[0] + 1] = consts.SOLDIER_PLACEMENT


def soldier_feet(game_field_metrics):
    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT:
                # takes top left corner of the soldier
                corner = (row, col)
                legs_position = []
                # a loop for the ammount of legs the soldier has, takes the cell each leg has and returns it in a list
                for legs in range(consts.SOLDIER_WIDTH):
                    legs_position.append([corner[0] + consts.SOLDIER_BODY, corner[1] + legs])
                return legs_position


def soldier_body(game_field_metrics):
    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT:
                corner = (row, col)
                body_position = []
                for height in range(consts.SOLDIER_BODY):
                    for i in range(consts.SOLDIER_WIDTH):
                        body_position.append([corner[0] + height, corner[1] + i])
                return body_position


def get_soldier_pos(game_field_metrics):
    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT:
                return col, row
