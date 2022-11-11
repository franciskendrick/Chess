from window import window
from screens import Background
from .titles import Titles
import pygame

pygame.init()


class Questions:
    display_size_divider = 2

    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        self.background = Background()
        self.titles = Titles()

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
        self.titles.draw(self.display)

        # Blit to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
