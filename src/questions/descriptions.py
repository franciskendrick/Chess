from utils import clip_set_to_list_on_xaxis, separate_sets_from_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "questions"
        )
    )

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/descriptions.png"), (255, 0, 0))


class PlayAsDescription:
    # Initialize
    def __init__(self):
        # Images
        order = ["white", "random", "black"]
        images = clip_set_to_list_on_xaxis(spritesets[0])

        # Positions
        positions = {
            "white": (103, 94),
            "random": (141, 94),
            "black": (187, 94)
        }

        # Buttons
        self.descriptions = {}
        for name, img in zip(order, images):
            self.descriptions[name] = [
                img,  # image
                pygame.Rect(positions[name], img.get_rect().size)  # rectangle
            ]

    # Draw
    def draw(self, display):
        for img, rect in self.descriptions.values():
            # Blit to display
            display.blit(img, rect)
