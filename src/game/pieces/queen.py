from .piece import Piece
import pygame

pygame.init()


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

    def valid_moves(self, board):
        pass