from .piece import Piece
import pygame

pygame.init()


class Rook(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][2]
        self.offset = (3, 1)

    def valid_moves(self, board, _):
        row = self.row
        col = self.col

        valid_moves = []

        # Top
        for y in range(row - 1, -1, -1):
            square = board[y][col]
            if square == 0:  # if an empty square
                valid_moves.append((0, col, y))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((1, col, y))
                break
            else:  # if there is an ally piece
                break

        # Bottom
        for y in range(row + 1, 8):
            square = board[y][col]
            if square == 0:  # if an empty square
                valid_moves.append((0, col, y))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((1, col, y))
                break
            else:  # if there is an ally piece
                break

        # Left
        for x in range(col - 1, -1, -1):
            square = board[row][x]
            if square == 0:  # if an empty square
                valid_moves.append((0, x, row))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((1, x, row))
                break
            else:  # if there is an ally piece
                break

        # Right
        for x in range(col + 1, 8):
            square = board[row][x]
            if square == 0:  # if an empty square
                valid_moves.append((0, x, row))
            elif square.color != self.color:  # if there is a opponent piece
                valid_moves.append((1, x, row))
                break
            else:  # if there is an ally piece
                break

        # Return
        return valid_moves
