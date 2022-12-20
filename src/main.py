from window import window
from menu import Menu
from questions import Questions
import pygame
import sys


# Redraws
def redraw_menu():
    # Draw background
    win.fill((77, 43, 50))

    # Draw menu
    menu.draw_background(win)
    menu.draw_foreground(win)

    # Update display
    pygame.display.update()


def redraw_questions():
    # Draw background
    win.fill((77, 43, 50))

    # Draw questions
    questions.draw_background(win)
    questions.draw_foreground(win)
     
    # Update display
    pygame.display.update()


def redraw_game():
    # Update display
    pygame.display.update()


# Loops
def menu_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

                # Update questions' settings' JSON
                questions_settings = {
                    "play_as": questions.playas_buttons,
                    "play_vs": questions.playvs_buttons,
                    "chess_clock": questions.chessclock_buttons
                }
                window.update_questionssettings(questions_settings)

            # Menu buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                button_pressed = menu.buttons.button_down_detection()
                if button_pressed == "play":
                    menu.buttons.reset_overdetection()
                    questions_loop(menu_loop)
                elif button_pressed == "options":
                    pass  # !!!

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.buttons.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def questions_loop(from_loop):
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

                # Update questions' settings' JSON
                questions_settings = {
                    "play_as": questions.playas_buttons,
                    "play_vs": questions.playvs_buttons,
                    "chess_clock": questions.chessclock_buttons
                }
                window.update_questionssettings(questions_settings)

            # Question buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                # Toggle buttons
                questions.playas_buttons.button_down_detection()
                questions.playvs_buttons.button_down_detection()
                questions.chessclock_buttons.button_down_detection()

                # Text buttons
                button_pressed = questions.blue_buttons.button_down_detection()
                if button_pressed == "back":
                    questions.buttons_reset_overdetection()
                    from_loop()
                elif button_pressed == "reset":
                    questions.reset()
                elif button_pressed == "next":
                    pass  # !!!

            # Question buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                # Toggle buttons
                questions.playas_buttons.button_over_detection()
                questions.playvs_buttons.button_over_detection()
                questions.chessclock_buttons.button_over_detection()

                # Text buttons
                questions.blue_buttons.button_over_detection()

        # Update display
        redraw_questions()
        clock.tick(window.framerate)

    pygame.quit()
    sys.exit()


def game_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

                # Update questions' settings' JSON
                questions_settings = {
                    "play_as": questions.playas_buttons,
                    "play_vs": questions.playvs_buttons,
                    "chess_clock": questions.chessclock_buttons
                }
                window.update_questionssettings(questions_settings)

        # Update display
        redraw_game()

    pygame.quit()
    sys.exit()


# Execute
if __name__ == "__main__":
    pygame.init()

    # Initialize window
    win = pygame.display.set_mode(window.rect.size)  # !!!
    # win = pygame.display.set_mode(window.win_size)
    pygame.display.set_caption("Chess")
    clock = pygame.time.Clock()
    
    # Initialize windows
    menu = Menu()
    questions = Questions()

    # Execute
    menu_loop()
