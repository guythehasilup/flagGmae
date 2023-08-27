import consts
import game_field
import guard
import main


def soldier_move_left(game_field_metrics, state):
    feet_location = soldier_feet(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    if soldier_placement[0] - 1 < 0:
        return
    elif (game_field_metrics[feet_location[0][0]][feet_location[0][1] - 1] == consts.MINE_PLACEMENT or
          is_touching_guard(soldier_placement)):
        loss(state, feet_location)
        return
    # move soldier left
    # remove the rightest side of soldier
    for row in range(consts.SOLDIER_HEIGHT):
        game_field_metrics[soldier_placement[1] + row][soldier_placement[0] + 1] = consts.EMPTY_PLACEMENT
    # add soldier from the left
    for row in range(consts.SOLDIER_HEIGHT):
        game_field_metrics[soldier_placement[1] + row][soldier_placement[0] - 1] = consts.SOLDIER_PLACEMENT
    game_field.restore_mines()


def soldier_move_right(game_field_metrics, state):
    win_con = 0
    feet_location = soldier_feet(game_field_metrics)
    body_location = soldier_body(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    if feet_location[1][1] + 1 >= consts.MATRIX_WIDTH:
        return
    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            # Win condition, body on the flag
            if ([body_location[3][0], body_location[3][1]] == game_field.flag[0][0] or
                    [body_location[5][0], body_location[5][1]] == game_field.flag[1][0]):
                win_con = 1
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT:
                if ((game_field_metrics[feet_location[1][0]][feet_location[1][1] + 1]) == consts.MINE_PLACEMENT or
                        is_touching_guard(soldier_placement)):
                    loss(state, feet_location)
                    return
                else:
                    # moves soldier right
                    for i in range(consts.SOLDIER_HEIGHT):
                        game_field_metrics[row + i][col] = consts.EMPTY_PLACEMENT
                        game_field_metrics[row + i][col + 1] = consts.SOLDIER_PLACEMENT
                        game_field_metrics[row + i][col + 2] = consts.SOLDIER_PLACEMENT
                        game_field.restore_mines()
                        if win_con == 1:
                            state["is_won"] = True
                            return
                    return


def soldier_move_down(game_field_metrics, state):
    win_con = 0
    feet_location = soldier_feet(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    body_location = soldier_body(game_field_metrics)
    if feet_location[0][0] + 1 == consts.MATRIX_HEIGHT:
        return
    elif (game_field_metrics[feet_location[0][0] + 1][feet_location[0][1]] == consts.MINE_PLACEMENT or
          game_field_metrics[feet_location[1][0] + 1][feet_location[1][1]] == consts.MINE_PLACEMENT or
          is_touching_guard(soldier_placement)):
        loss(state, feet_location)
        return
    elif down_win(body_location):
        win_con = 1
    # move soldier down
    game_field_metrics[soldier_placement[1]][soldier_placement[0]] = consts.EMPTY_PLACEMENT
    game_field_metrics[soldier_placement[1]][soldier_placement[0] + 1] = consts.EMPTY_PLACEMENT
    game_field_metrics[soldier_placement[1] + consts.SOLDIER_HEIGHT][
        soldier_placement[0]] = consts.SOLDIER_PLACEMENT
    game_field_metrics[soldier_placement[1] + consts.SOLDIER_HEIGHT][
        soldier_placement[0] + 1] = consts.SOLDIER_PLACEMENT
    game_field.restore_mines()
    if win_con == 1:
        state["is_won"] = True


def soldier_move_up(game_field_metrics, state):
    feet_location = soldier_feet(game_field_metrics)
    soldier_placement = get_soldier_pos(game_field_metrics)
    if soldier_placement[1] - 1 < 0:
        return
    elif (game_field_metrics[feet_location[0][0] - 1][feet_location[0][1]] == consts.MINE_PLACEMENT or
          game_field_metrics[feet_location[1][0] - 1][feet_location[1][1]] == consts.MINE_PLACEMENT or
          is_touching_guard(soldier_placement)):
        loss(state, feet_location)
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
    game_field.restore_mines()


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


def loss(state, feet_location):
    # displays the loss when I step on a mine
    state["is_lost"] = True
    state["soldier_feet_pos"] = feet_location
    consts.SOLDIER_IMAGE = consts.INJURED_SOLDIER_IMAGE


def down_win(body_location):
    flag = game_field.flag
    # checks if the cell the body is going to has a flag in it
    for i in range(consts.SOLDIER_WIDTH):
        for j in range(consts.FLAG_WIDTH):
            if [body_location[4 + i][0] + 1, body_location[4 + i][1]] == flag[0][j]:
                return True


def right_win(body_location):
    flag = game_field.flag
    for i in range(2):
        for j in range(consts.FLAG_WIDTH):
            if [body_location[2 + i][0] + 1, body_location[3 + i][1]] == flag[0][j]:
                return True
    # ([body_location[3][0], body_location[3][1] + 1] == game_field.flag[0][0] or
    #  [body_location[5][0], body_location[5][1] + 1] == game_field.flag[1][0]):


def is_touching_guard(soldier_pos):
    for row in range(consts.SOLDIER_HEIGHT):
        for col in range(consts.SOLDIER_WIDTH):
            if ([row + soldier_pos[1], col + soldier_pos[0]] in guard.guard_index[0] or
                    [row + soldier_pos[1], col + soldier_pos[0]] in guard.guard_index[1]):
                return True
    return False
