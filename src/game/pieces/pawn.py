from .piece import Piece
import pygame

pygame.init()


class Pawn(Piece):
    def __init__(self, row, col, color, play_as):
        super().__init__(row, col, color)

        self.image = self.images[color][5]
        self.offset = (4, 3)
        self.play_as = play_as
        self.first_move = True

    def valid_moves(self, board, last_move):
        row = self.row
        col = self.col

        valid_moves = []

        if self.play_as[0] == self.color:  # hence, moves upward
            if row > 0:
                # Moving at Top Middle
                square = board[row - 1][col]
                if square == 0:
                    valid_moves.append((0, col, row - 1))

                if self.first_move and board[row - 1][col] == 0:
                    square = board[row - 2][col]
                    if square == 0:
                        valid_moves.append((0, col, row - 2))

                # Eating at Top Left
                square = board[row - 1][col - 1]
                if square != 0 and square.color != self.color:
                    valid_moves.append((1, col - 1, row - 1))

                # Eating at Top Right
                square = board[row - 1][col + 1]
                if square != 0 and square.color != self.color:
                    valid_moves.append((1, col + 1, row - 1))

                # En Passant
                if last_move != None and last_move["piece"] == Pawn:
                    # En Passant at Left
                    if last_move["current"] == (row, col - 1):
                        valid_moves.append((2, col - 1, row - 1))

                    # En Passant at Right
                    if last_move["current"] == (row, col + 1):
                        valid_moves.append((2, col + 1, row - 1))

        else:  # hence, moves downward
            if row < 7:
                # Moving at Bottom Middle
                square = board[row + 1][col]
                if square == 0:
                    valid_moves.append((0, col, row + 1))

                if self.first_move and board[row + 1][col] == 0:
                    square = board[row + 2][col]
                    if square == 0:
                        valid_moves.append((0, col, row + 2))

                # Eating at Bottom Left
                square = board[row + 1][col - 1]
                if square != 0 and square.color != self.color:
                    valid_moves.append((1, col - 1, row + 1))

                # Eating at Bottom Right
                square = board[row + 1][col + 1]
                if square != 0 and square.color != self.color:
                    valid_moves.append((1, col + 1, row + 1))

                # En Passant
                if last_move != None and last_move["piece"] == Pawn:
                    # En Passant at Left
                    if last_move["current"] == (row, col - 1):
                        valid_moves.append((2, col - 1, row + 1))

                    # En Passant at Right
                    if last_move["current"] == (row, col + 1):
                        valid_moves.append((2, col + 1, row + 1))

        # Return
        return valid_moves
