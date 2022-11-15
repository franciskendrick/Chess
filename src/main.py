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

            # Menu buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                button_pressed = menu.buttons.button_down_detection()

            # Menu buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                menu.buttons.button_over_detection()

        # Update display
        redraw_menu()
        clock.tick(30)

    pygame.quit()
    sys.exit()


def questions_loop():
    # Loop
    run = True
    while run:
        # Event loop
        for event in pygame.event.get():
            # Quit detection
            if event.type == pygame.QUIT:
                run = False

            # Question buttons' down detection
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # left-clicked has been uped
                questions.playvswho_buttons.button_down_detection()

            # Question buttons' over detection
            if event.type == pygame.MOUSEMOTION:
                questions.playvswho_buttons.button_over_detection()

        # Update display
        redraw_questions()

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
    questions_loop()
