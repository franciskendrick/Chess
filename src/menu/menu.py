from window import window
from .background import Background
from .title import Title
from .buttons import Buttons
import pygame

pygame.init()


class Menu:
    display_size_divider = 4

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        self.background = Background()
        self.title = Title()
        self.buttons = Buttons(self.display_size_divider)

    def draw_background(self, display):
        # Draw background on display
        self.background.draw(self.display)

        # Blit to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))

    def draw_foreground(self, display):
        # Fill display with an opaque background
        self.display.fill((77, 43, 50, 180))

        # Draw foreground on display
        self.title.draw(self.display)
        self.buttons.draw(self.display)

        # Blit to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
