import pygame

pygame.init()


class Piece:
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
