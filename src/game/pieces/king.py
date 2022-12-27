from .piece import Piece
import pygame

pygame.init()


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][0]

    def valid_moves(self, board):
        pass
