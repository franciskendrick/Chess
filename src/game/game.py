from window import window
from screens import Background
import pygame

pygame.init()


class Game:
    def __init__(self):
        self.display = pygame.Surface(
            window.rect.size, pygame.SRCALPHA)

        self.background = Background()

    def draw_background(self, display):
        # Draw background on display
        self.background.draw(self.display)

        # Blit to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))

    def draw_foreground(self, display):
        pass