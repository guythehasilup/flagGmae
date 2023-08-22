import consts
import game_field
import main


def soldier_move_left(game_field_metrics):

    feet_location = soldier_feet(game_field_metrics)

    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT and row - 3 < consts.MATRIX_HEIGHT:
                if (game_field_metrics[feet_location[1][0] + 1][feet_location[1][1]]) == consts.MINE_PLACEMENT:
                    main.state["is_lost"] = True
                    return
                else:
                    for i in range(consts.SOLDIER_HEIGHT):
                        game_field_metrics[row][col + i] = consts.EMPTY_PLACEMENT
                        game_field_metrics[row - 1][col + i] = consts.SOLDIER_PLACEMENT
                        game_field_metrics[row - 2][col + i] = consts.SOLDIER_PLACEMENT
                    return


def soldier_move_right(game_field_metrics):

    feet_location = soldier_feet(game_field_metrics)

    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT and row + 1 < consts.MATRIX_HEIGHT:
                if (game_field_metrics[feet_location[1][0] + 1][feet_location[1][1]]) == consts.MINE_PLACEMENT:
                    main.state["is_lost"] = True
                    return
                else:
                    for i in range(consts.SOLDIER_HEIGHT):
                        game_field_metrics[row][col + i] = consts.EMPTY_PLACEMENT
                        game_field_metrics[row + 1][col + i] = consts.SOLDIER_PLACEMENT
                        game_field_metrics[row + 2][col + i] = consts.SOLDIER_PLACEMENT
                    return


def soldier_move_down(game_field_metrics):
    feet_location = soldier_feet(game_field_metrics)

    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT and col + 2 < consts.MATRIX_WIDTH:
                if (game_field_metrics[feet_location[1][0]][feet_location[1][1] + 1]) == consts.MINE_PLACEMENT:
                    main.state["is_lost"] = True
                    return
                else:
                    for i in range(consts.SOLDIER_HEIGHT):
                        game_field_metrics[row + i][col] = consts.EMPTY_PLACEMENT
                        game_field_metrics[row + i][col + 1] = consts.SOLDIER_PLACEMENT
                        game_field_metrics[row + i][col + 2] = consts.SOLDIER_PLACEMENT
                    return




def soldier_move_up(game_field_metrics):
    feet_location = soldier_feet(game_field_metrics)

    for row in range(len(game_field_metrics)):
        for col in range(len(game_field_metrics[row])):
            if game_field_metrics[row][col] == consts.SOLDIER_PLACEMENT and col - 2 >= 0:
                if (game_field_metrics[feet_location[1][0]][feet_location[1][1] - 1]) == consts.MINE_PLACEMENT:
                    main.state["is_lost"] = True
                    return
                else:
                    for i in range(consts.SOLDIER_HEIGHT):
                        game_field_metrics[row + i][col + 1] = consts.EMPTY_PLACEMENT
                        game_field_metrics[row + i][col - 1] = consts.SOLDIER_PLACEMENT
                        game_field_metrics[row + i][col - 2] = consts.SOLDIER_PLACEMENT
                    return



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
                return row, col
