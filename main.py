
import os
import time

import pygame

import consts
import database
import game_field
import guard
import screen
import soldier
import teleport

state = {
    "is_window_open": True,
    "is_lost": False,
    "is_lost_by_guard": False,
    "is_won": False,
    "state": consts.RUNNING_STATE
}


def main():
    file_exists = os.path.exists(consts.DATABASE_FILE)
    if not file_exists:
        database.initialize_db()
    pygame.init()
    game_field.initiate_empty_game_field()
    game_field.initiate_game_field()
    screen.set_bush_placement()
    # game_field.print_board()
    # print(game_field.mines)
    while state["is_window_open"]:
        if state["state"] is consts.RUNNING_STATE:
            handle_events()
            screen.draw_game(state)
            if state["is_lost"] or state["is_won"]:
                state["state"] = consts.ENG_GAME_STATE
        else:
            if state["is_lost"]:
                if state["is_lost_by_guard"]:
                    guard_pos = guard.get_guard_pos()
                    screen.draw_explosion(guard_pos[0] * consts.SQUARE_EDGE, (guard_pos[1] - consts.EXPLOSION_HEIGHT + consts.GUARD_HEIGHT) * consts.SQUARE_EDGE)
                else:
                    screen.draw_lose_screen()
                pygame.display.update()
                pygame.time.delay(3000)
                state["is_window_open"] = False
            if state["is_won"]:
                screen.draw_win_screen()
                pygame.display.update()
                pygame.time.delay(3000)
                state["is_window_open"] = False


def handle_events():
    global time_down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                soldier.soldier_move_left(game_field.game_field_metrics, state)
            elif event.key == pygame.K_RIGHT:
                soldier.soldier_move_right(game_field.game_field_metrics, state)
            elif event.key == pygame.K_UP:
                soldier.soldier_move_up(game_field.game_field_metrics, state)
            elif event.key == pygame.K_DOWN:
                soldier.soldier_move_down(game_field.game_field_metrics, state)
            elif event.key == pygame.K_RETURN:
                screen.draw_night_vision_game()
                pygame.display.update()
                pygame.time.delay(1000)
            elif event.key == pygame.K_1:
                time_down = time.time()
            elif event.key == pygame.K_2:
                time_down = time.time()
            elif event.key == pygame.K_3:
                time_down = time.time()
            elif event.key == pygame.K_4:
                time_down = time.time()
            elif event.key == pygame.K_5:
                time_down = time.time()
            elif event.key == pygame.K_6:
                time_down = time.time()
            elif event.key == pygame.K_7:
                time_down = time.time()
            elif event.key == pygame.K_8:
                time_down = time.time()
            elif event.key == pygame.K_9:
                time_down = time.time()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(1)
                else:
                    database.save_game(1)
            elif event.key == pygame.K_2:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(2)
                else:
                    database.save_game(2)
            elif event.key == pygame.K_3:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(3)
                else:
                    database.save_game(3)

            elif event.key == pygame.K_4:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(4)
                else:
                    database.save_game(4)
            elif event.key == pygame.K_5:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(5)
                else:
                    database.save_game(5)

            elif event.key == pygame.K_6:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(6)
                else:
                    database.save_game(6)
            elif event.key == pygame.K_7:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(7)
                else:
                    database.save_game(7)

            elif event.key == pygame.K_8:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(8)
                else:
                    database.save_game(8)
            elif event.key == pygame.K_9:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    load_game(9)
                else:
                    database.save_game(9)


def load_game(key):
    if eval(database.read_db(key, consts.VAR_SOLDIER)):
        game_field.clear_board()
        game_field.initiate_guard_pos()
        game_field.set_soldier_pos(eval(database.read_db(key, consts.VAR_SOLDIER)))
        game_field.mines = []
        game_field.set_mines_pos(eval(database.read_db(key, consts.VAR_MINE)))
        consts.BUSH_PLACEMENT = eval(database.read_db(key, consts.VAR_BUSH))
        teleport.teleports = []
        teleport.reset_teleports_to_matrix(eval(database.read_db(key, consts.VAR_TELEPORT)))


if __name__ == "__main__":
    main()
