from utils import separate_sets_from_yaxis, clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", "resources", "game"
        )
    )

white_spriteset, black_spriteset = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/pieces.png"))


class Piece:
    images = {
        "w": clip_set_to_list_on_xaxis(white_spriteset),  # white
        "b": clip_set_to_list_on_xaxis(black_spriteset)  # black
    }

    def __init__(self, row, col, color):
        # Position
        self.row = row
        self.col = col

        # Color
        self.color = color

        # Status
        self.is_selected = False

    def draw(self, display):
        pass
