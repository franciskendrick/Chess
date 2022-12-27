from .piece import Piece
import pygame

pygame.init()


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][4]
        self.offset = (2, 1)

    def valid_moves(self, board):
        pass
