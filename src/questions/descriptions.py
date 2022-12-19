from utils import clip_set_to_list_on_xaxis, clip_set_to_list_on_yaxis, separate_sets_from_xaxis, separate_sets_from_yaxis
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


class PlayVsDescription:
    # Initialize
    def __init__(self):
        # Images
        self.order = ["easy", "medium", "hard"]
        spritesets_ = separate_sets_from_xaxis(spritesets[1], (255, 0, 0))

        # Positions
        positions = {
            "easy": (48, 160),
            "medium": (130, 160),
            "hard": (216, 160)
        }

        # Buttons
        self.descriptions = {}
        for name, spriteset in zip(self.order, spritesets_):
            images = clip_set_to_list_on_yaxis(spriteset)
            self.descriptions[name] = [
                0,  # idx
                images,  # image
                pygame.Rect(positions[name], images[0].get_rect().size)  # rectangle
            ]
        
        # Animation
        self.idx_addingto = 0

    # Draw
    def draw(self, display):
        for name, (_, images, rect) in self.descriptions.items():
            # Reset
            if self.descriptions[self.order[self.idx_addingto]][0] >= (len(images)) * 10:
                self.idx_addingto += 1
                if self.idx_addingto >= len(self.order):
                    self.idx_addingto = 0
                    for name_ in self.descriptions.keys():
                        self.descriptions[name_][0] = 0  # idx
            
            # Blit to display
            idx = self.descriptions[name][0]
            display.blit(images[idx // 10], rect)

            # Update
            self.descriptions[self.order[self.idx_addingto]][0] += 1  # idx
