import game_field
import pygame
import screen

state = {
    "is_window_open": True
}


def main():
    pygame.init()
    clock = pygame.time.Clock()
    game_field.initiate_empty_game_field()
    game_field.initiate_game_field()
    # game_field.print_board()
    print(game_field.mines)
    while state["is_window_open"]:
        handle_events()
        screen.draw_game()
        # do something or crash
        # print(2)
        # pygame.display.update()
        # clock.tick(60)


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state["is_window_open"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass
            if event.key == pygame.K_RETURN:
                screen.draw_night_vision_game()
                pygame.display.update()
                pygame.time.delay(1000)


if __name__ == "__main__":
    main()
