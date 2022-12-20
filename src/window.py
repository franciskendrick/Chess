import pygame
import json
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "resources"
        )
    )


class Window:
    # Window
    rect = pygame.Rect(0, 0, 640, 640)
    enlarge = (pygame.display.Info().current_h - 80) / rect.height
    win_size = (int(rect.width * enlarge), int(rect.height * enlarge))

    # Initialize
    def __init__(self):
        # Saved questions settings
        with open(f"{resources_path}/questions/settings.json") as json_file:
            self.saved_questions_settings = json.load(json_file)

    # Update
    def update_questionssettings(self, questions_settings):
        # Get handle settings
        handle_settings = self.saved_questions_settings.copy()

        # Edit questions' settings
        for json_key, questions_buttons in zip(
                handle_settings.keys(), questions_settings.values()):
            for (name, button) in questions_buttons.buttons.items():
                if button[1]:  # buttons' toggle status is True
                    handle_settings[json_key] = name
                    break
        
        # Dump handle settings to the JSON file
        with open(f"{resources_path}/questions/settings.json", "w") as json_file:
            json.dump(handle_settings, json_file)


window = Window()
