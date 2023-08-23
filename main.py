import os
import time

import database
import game_field
import pygame
import screen
import consts
import soldier

state = {
    "is_window_open": True,
    "is_lost": False,
    "is_won": False,
    "state": consts.RUNNING_STATE,
    "soldier_feet_pos": []
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
            screen.draw_game()
            if state["is_lost"] or state["is_won"]:
                state["state"] = consts.ENG_GAME_STATE

            # do something or crash
            # pygame.display.update()
            # clock.tick(60)
        else:
            if state["is_lost"]:
                screen.draw_lose_screen()
                screen.draw_explosion(state["soldier_feet_pos"][0][1] * consts.SQUARE_EDGE,
                                      state["soldier_feet_pos"][0][0] * consts.SQUARE_EDGE)
                pygame.display.update()
                pygame.time.delay(3000)
                state["is_window_open"] = False
            if state["is_won"]:
                screen.draw_win_screen()
                pygame.display.update()
                pygame.time.delay(3000)
                state["is_window_open"] = False


def handle_events():
    # time_down = time.time()
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
            # elif event.key == pygame.K_2:
            #     time_down = time.time()
            # elif event.key == pygame.K_3:
            #     time_down = time.time()
            # elif event.key == pygame.K_4:
            #     time_down = time.time()
            # elif event.key == pygame.K_5:
            #     time_down = time.time()
            # elif event.key == pygame.K_6:
            #     time_down = time.time()
            # elif event.key == pygame.K_7:
            #     time_down = time.time()
            # elif event.key == pygame.K_8:
            #     time_down = time.time()
            # elif event.key == pygame.K_9:
            #     time_down = time.time()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                time_elapsed = time.time() - time_down
                if time_elapsed <= 1:
                    print("load")
                else:
                    database.save_game(1)
            # elif event.key == pygame.K_2:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            # elif event.key == pygame.K_3:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            #
            # elif event.key == pygame.K_4:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            # elif event.key == pygame.K_5:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            #
            # elif event.key == pygame.K_6:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            #
            # elif event.key == pygame.K_7:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            #
            # elif event.key == pygame.K_8:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")
            # elif event.key == pygame.K_9:
            #     time_elapsed = time.time() - time_down
            #     if time_elapsed <= 1:
            #         print("load")
            #     else:
            #         print("save")


if __name__ == "__main__":
    main()
