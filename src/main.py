from window import window
from menu import Menu
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

        # Update display
        redraw_menu()
        clock.tick(30)

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

    # Execute
    menu_loop()
