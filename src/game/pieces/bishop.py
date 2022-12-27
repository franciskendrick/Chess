from .piece import Piece
import pygame

pygame.init()


class Bishop(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][3]
        self.offset = (3, 1)

    def valid_moves(self, board):
        pass
