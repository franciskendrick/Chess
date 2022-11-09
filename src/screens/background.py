from utils import clip_set_to_list_on_xaxis
from window import window
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "screens"
        )
    )


class Background:
    def __init__(self, enlarge=4):
        self.enlarge = enlarge

        # Display
        wd, ht = window.rect.size
        self.display = pygame.Surface(
            (wd // self.enlarge, ht // self.enlarge),
            pygame.SRCALPHA)

        # Board
        img = pygame.image.load(f"{resources_path}/board.png")
        wd, ht = img.get_size()
        self.board = [
            pygame.transform.scale(img, (wd * 2, ht * 2)),
            (14, 14)
        ]

        # Lattice
        self.lattice_imgs = clip_set_to_list_on_xaxis(
            pygame.image.load(f"{resources_path}/lattice.png"))
        self.lattice_pos = [  # format: x, y, number of cells, index of first cell
            (2, 22, 3, 0),
            (2, 50, 8, 0),
            (2, 113, 3, 1),
            (148, 22, 3, 1),
            (148, 50, 8, 1),
            (148, 113, 3, 0)
        ]
        self.cell_width = 7  # width of a cell

    def draw(self, display):
        # Draw board
        self.display.blit(*self.board)

        # Draw lattice
        for (x, y, num, idx) in self.lattice_pos:
            for i in range(num):
                self.display.blit(self.lattice_imgs[idx], (x, y + (i * self.cell_width)))
                idx = 0 if idx == 1 else 1

        # Blit to original display
        resized_menu_display = pygame.transform.scale(
            self.display, display.get_size())
        display.blit(resized_menu_display, (0, 0))
