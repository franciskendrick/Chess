from .pieces import King, Queen, Rook, Bishop, Knight, Pawn
import pygame

pygame.init()


class Board:
    board_truesize = (512, 512)

    # Initialize
    def __init__(self):
        # Board
        self.board_surface = pygame.Surface((128, 128), pygame.SRCALPHA)
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.rects = [[pygame.Rect(x, y, 16, 16) for x in range(0, 16*8, 16)] for y in range(0, 16*8, 16)]

        # self.init_pieces()
        self.board[0][6] = Knight(0, 6, "w")  # !!! TEMPORARY

        # Action detection
        self.previously_selected = None

    def init_pieces(self):  # !!! TEMPORARY
        # Black
        self.board[0][0] = Rook(0, 0, "b")
        self.board[0][1] = Knight(0, 1, "b")
        self.board[0][2] = Bishop(0, 2, "b")
        self.board[0][3] = Queen(0, 3, "b")
        self.board[0][4] = King(0, 4, "b")
        self.board[0][5] = Bishop(0, 5, "b")
        self.board[0][6] = Knight(0, 6, "b")
        self.board[0][7] = Rook(0, 7, "b")

        self.board[1][0] = Pawn(1, 0, "b")
        self.board[1][1] = Pawn(1, 1, "b")
        self.board[1][2] = Pawn(1, 2, "b")
        self.board[1][3] = Pawn(1, 3, "b")
        self.board[1][4] = Pawn(1, 4, "b")
        self.board[1][5] = Pawn(1, 5, "b")
        self.board[1][6] = Pawn(1, 6, "b")
        self.board[1][7] = Pawn(1, 7, "b")

        # White
        self.board[7][0] = Rook(7, 0, "w")
        self.board[7][1] = Knight(7, 1, "w")
        self.board[7][2] = Bishop(7, 2, "w")
        self.board[7][3] = Queen(7, 3, "w")
        self.board[7][4] = King(7, 4, "w")
        self.board[7][5] = Bishop(7, 5, "w")
        self.board[7][6] = Knight(7, 6, "w")
        self.board[7][7] = Rook(7, 7, "w")

        self.board[6][0] = Pawn(6, 0, "w")
        self.board[6][1] = Pawn(6, 1, "w")
        self.board[6][2] = Pawn(6, 2, "w")
        self.board[6][3] = Pawn(6, 3, "w")
        self.board[6][4] = Pawn(6, 4, "w")
        self.board[6][5] = Pawn(6, 5, "w")
        self.board[6][6] = Pawn(6, 6, "w")
        self.board[6][7] = Pawn(6, 7, "w")

    # Draw
    def draw(self, display):
        self.board_surface.fill((0, 0, 0, 0))

        # Draw board on board's surface
        for row in self.board:
            for square in row:
                if square != 0:  # if not an empty square
                    # Blit to board's surface
                    square.draw(
                        self.board_surface, square.valid_moves(self.board))

        # Blit to game's display
        resized_board_surface = pygame.transform.scale(
            self.board_surface, self.board_truesize)
        display.blit(resized_board_surface, (64, 64))

    # Action detection
    def down_detection(self):
        # Updated previously selected's "selected" status to false
        if self.previously_selected != None:
            self.previously_selected.is_selected = False

        # Get the square where mouse is clicked
        mouse_pos = pygame.mouse.get_pos()
        for y, row in enumerate(self.board):
            for x, square in enumerate(row):
                if square != 0:  # if not an empty square
                    # Get hitbox
                    rect = self.rects[y][x]
                    hitbox = pygame.Rect(
                        rect.x * 4 + 64, rect.y * 4 + 64, 64, 64)

                    # Check if rectangle is colliding with mouse's position
                    if hitbox.collidepoint(mouse_pos):
                        square.is_selected = True
                        self.previously_selected = square
                        break
