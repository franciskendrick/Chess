from .piece import Piece
import pygame

pygame.init()


class Knight(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][4]
        self.offset = (2, 1)

    def valid_moves(self, board):
        row = self.row
        col = self.col

        valid_moves = []

        # Up-Left
        if row > 1 and col > 0:
            square = board[row - 2][col - 1]
            if square == 0:  # if an empty square
                valid_moves.append((col - 1, row - 2))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col - 1, row - 2))

        # Up-Right
        if row > 1 and col < 7:
            square = board[row - 2][col + 1]
            if square == 0:  # if an empty square
                valid_moves.append((col + 1, row - 2))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col + 1, row - 2))

        # Down-Left
        if row < 6 and col > 0:
            square = board[row + 2][col - 1]
            if square == 0:  # if an empty square
                valid_moves.append((col - 1, row + 2))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col - 1, row + 2))

        # Down-Right
        if row < 6 and col < 7:
            square = board[row + 2][col + 1]
            if square == 0:  # if an empty square
                valid_moves.append((col + 1, row + 2))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col + 1, row + 2))

        # Left-Up
        if row > 0 and col > 1:
            square = board[row - 1][col - 2]
            if square == 0:  # if an empty square
                valid_moves.append((col - 2, row - 1))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col - 2, row - 1))

        # Left-Down
        if row < 7 and col > 1:
            square = board[row + 1][col - 2]
            if square == 0:  # if an empty square
                valid_moves.append((col - 2, row + 1))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col - 2, row + 1))

        # Right-Up
        if row > 0 and col < 6:
            square = board[row - 1][col + 2]
            if square == 0:  # if an empty square
                valid_moves.append((col + 2, row - 1))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col + 2, row - 1))

        # Right-Down
        if row < 7 and col < 6:
            square = board[row + 1][col + 2]
            if square == 0:  # if an empty square
                valid_moves.append((col + 2, row + 1))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((col + 2, row + 1))

        # Return
        return valid_moves
