import game_field
import pygame
import screen
import consts
import soldier

state = {
    "is_window_open": True,
    "is_lost": False,
    "is_won": False,
    "state": consts.RUNNING_STATE
}


def main():
    pygame.init()
    clock = pygame.time.Clock()
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
            # print(2)
            # pygame.display.update()
            # clock.tick(60)
        else:
            pass


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                soldier.soldier_move_left(game_field.game_field_metrics)
            if event.key == pygame.K_RIGHT:
                soldier.soldier_move_right(game_field.game_field_metrics)
            if event.key == pygame.K_UP:
                soldier.soldier_move_up(game_field.game_field_metrics)
            if event.key == pygame.K_DOWN:
                soldier.soldier_move_down(game_field.game_field_metrics)
            if event.key == pygame.K_RETURN:
                screen.draw_night_vision_game()
                pygame.display.update()
                pygame.time.delay(1000)


if __name__ == "__main__":
    main()
