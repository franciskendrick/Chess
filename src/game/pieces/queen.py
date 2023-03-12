from .piece import Piece
import pygame

pygame.init()


class Queen(Piece):
    def __init__(self, row, col, color):
        super().__init__(row, col, color)

        self.image = self.images[color][1]
        self.offset = (1, 1)

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

        # Top-right
        x = col + 1
        for y in range(row - 1, -1, -1):
            if x <= 7:
                square = board[y][x]
                if square == 0:  # if an empty square
                    valid_moves.append((0, x, y))
                elif square.color != self.color:  # if there is a opponent piece
                    valid_moves.append((1, x, y))
                    break
                else:  # if there is an ally piece
                    break
                
            x += 1
        
        # Top-left
        x = col - 1
        for y in range(row - 1, -1, -1):
            if x >= 0:
                square = board[y][x]
                if square == 0:  # if an empty square
                    valid_moves.append((0, x, y))
                elif square.color != self.color:  # if there is a opponent piece
                    valid_moves.append((1, x, y))
                    break
                else:  # if there is an ally piece
                    break

            x -= 1

        # Bottom-right
        x = col + 1
        for y in range(row + 1, 8):
            if x <= 7:
                square = board[y][x]
                if square == 0:  # if an empty square
                    valid_moves.append((0, x, y))
                elif square.color != self.color:  # if there is a opponent piece
                    valid_moves.append((1, x, y))
                    break
                else:  # if there is an ally piece
                    break

            x += 1
        
        # Bottom-Left
        x = col - 1
        for y in range(row + 1, 8):
            if x >= 0:
                square = board[y][x]
                if square == 0:  # if an empty square
                    valid_moves.append((0, x, y))
                elif square.color != self.color:  # if there is a opponent piece
                    valid_moves.append((1, x, y))
                    break
                else:  # if there is an ally piece
                    break

            x -= 1

        # Return
        return valid_moves
