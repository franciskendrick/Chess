from window import window
from screens import Background
from .titles import Titles
from .buttons import PlayAsButtons, PlayVsButtons, ChessClockButtons, BlueButtons
from .descriptions import PlayAsDescription, PlayVsDescription
import pygame

pygame.init()


class Questions:
    orig_questions_settings = {
        "play_as": "random",
        "play_vs": "medium",
        "chess_clock": "10min"
    }
    display_size_divider = 2

    # Initialize
    def __init__(self):
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.display_size_divider,
            ht // self.display_size_divider),
            pygame.SRCALPHA)

        self.background = Background()

        # Titles
        self.titles = Titles()

        # Buttons
        self.playas_buttons = PlayAsButtons(self.display_size_divider)
        self.playvs_buttons = PlayVsButtons(self.display_size_divider)
        self.chessclock_buttons = ChessClockButtons(self.display_size_divider)
        self.blue_buttons = BlueButtons(self.display_size_divider)

        # Descriptions
        self.playas_description = PlayAsDescription()
        self.playvs_description = PlayVsDescription()

    # Draw
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

        # Draw titles on display
        self.titles.draw(self.display)

        # Draw buttons on display
        self.playas_buttons.draw(self.display)
        self.playvs_buttons.draw(self.display)
        self.chessclock_buttons.draw(self.display)
        self.blue_buttons.draw(self.display)

        # Draw description on display
        self.playas_description.draw(self.display)
        self.playvs_description.draw(self.display)

        # Blit to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))

    # Functions
    def reset(self):
        questions_buttons = {
            "play_as": self.playas_buttons,
            "play_vs": self.playvs_buttons,
            "chess_clock": self.chessclock_buttons
        }

        # Turn off all buttons' toggle status
        for questions_button in questions_buttons.values():
            for button in questions_button.buttons.values():
                button[1] = False  # toggle status

        # Turn on the original values in buttons' toggle status
        for questions_button, original_value in zip(
                questions_buttons.values(), self.orig_questions_settings.values()):
            for (name, button) in questions_button.buttons.items():
                if name == original_value:
                    button[1] = True  # toggle status
                    break

    def buttons_reset_overdetection(self):
        self.playas_buttons.reset_overdetection()
        self.playvs_buttons.reset_overdetection()
        self.chessclock_buttons.reset_overdetection()
        self.blue_buttons.reset_overdetection()
