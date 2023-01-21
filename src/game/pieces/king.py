from .piece import Piece
import pygame

pygame.init()


class King(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][0]
        self.offset = (1, 1)

    def valid_moves(self, board):
        row = self.row
        col = self.col

        valid_moves = []

        # Top
        if row > 0:
            # Top Left
            if col > 0:
                square = board[row - 1][col - 1]
                if square == 0:
                    valid_moves.append((0, col - 1, row - 1))
                elif square.color != self.color:
                    valid_moves.append((1, col - 1, row - 1))

            # Top Middle
            square = board[row - 1][col]
            if square == 0:
                valid_moves.append((0, col, row - 1))
            elif square.color != self.color:
                valid_moves.append((1, col, row - 1))

            # Top Right
            if col < 7:
                square = board[row - 1][col + 1]
                if square == 0:
                    valid_moves.append((0, col + 1, row - 1))
                elif square.color != self.color:
                    valid_moves.append((1, col + 1, row - 1))


        # Bottom
        if row < 7:
            # Bottom Left
            if col > 0:
                square = board[row + 1][col - 1]
                if square == 0:
                    valid_moves.append((0, col - 1, row + 1))
                elif square.color != self.color:
                    valid_moves.append((1, col - 1, row + 1))

            # Bottom Middle
            square = board[row + 1][col]
            if square == 0:
                valid_moves.append((0, col, row + 1))
            elif square.color != self.color:
                valid_moves.append((1, col, row + 1))

            # Bottom Right
            if col < 7:
                square = board[row + 1][col + 1]
                if square == 0:
                    valid_moves.append((0, col + 1, row + 1))
                elif square.color != self.color:
                    valid_moves.append((1, col + 1, row + 1))

        # left Middle
        if col > 0:
            square = board[row][col - 1]
            if square == 0:
                valid_moves.append((0, col - 1, row))
            elif square.color != self.color:
                valid_moves.append((1, col - 1, row))

        # Right Middle
        if col < 7:
            square = board[row][col + 1]
            if square == 0:
                valid_moves.append((0, col + 1, row))
            elif square.color != self.color:
                valid_moves.append((1, col + 1, row))

        # Return
        return valid_moves
