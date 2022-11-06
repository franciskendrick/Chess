from utils import clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "menu"
        )
    )


class Background:
    def __init__(self):
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
        # Board
        display.blit(*self.board)

        # Lattice
        for (x, y, num, idx) in self.lattice_pos:
            for i in range(num):
                display.blit(self.lattice_imgs[idx], (x, y + (i * self.cell_width)))
                idx = 0 if idx == 1 else 1
