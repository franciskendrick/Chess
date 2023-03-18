from .pieces import King, Queen, Rook, Bishop, Knight, Pawn
import pygame

pygame.init()


class Board:
    # Board
    board_truesize = (512, 512)

    # Pieces
    pieces_arangement = {
        "white": [  # play as white
            "R", "N", "B", "Q", "K", "B", "N", "R"],
        "black": [  # play as black
            "R", "N", "B", "K", "Q", "B", "N", "R"]
    }
    pieces_switchcase = {
        "K": King,
        "Q": Queen,
        "R": Rook,
        "N": Knight,
        "B": Bishop
    }

    # Initialize
    def __init__(self):
        # Board
        self.board_surface = pygame.Surface((128, 128), pygame.SRCALPHA)
        self.board = [[0 for _ in range(8)] for _ in range(8)]
        self.rects = [[pygame.Rect(x, y, 16, 16) for x in range(0, 16*8, 16)] for y in range(0, 16*8, 16)]

        # Action detection
        self.previously_selected = None
        self.currently_selected = None
        self.last_move = None  # color, piece, from position, current position
        self.move_number = 0

    def init_pieces(self, play_as):
        color = ["b", "w"] if play_as == "white" else ["w", "b"]
        for i, piece in enumerate(self.pieces_arangement[play_as]):
            # Top
            self.board[0][i] = self.pieces_switchcase[piece](0, i, color[0])
            self.board[1][i] = Pawn(1, i, color[0], play_as)

            # Bottom
            self.board[7][i] = self.pieces_switchcase[piece](7, i, color[1])
            self.board[6][i] = Pawn(6, i, color[1], play_as)

    # Draw
    def draw(self, display):
        self.board_surface.fill((0, 0, 0, 0))

        # Draw board on board's surface
        pieces = []
        for row in self.board:
            for square in row:
                if square != 0:  # if not an empty square
                    # Draw valid moves
                    if square.is_selected:
                        if self.move_number == 0 and square.color == "w" or (  # first move or selected piece is not equal to last move's color
                                square.color != self.last_move["color"]):
                            for (is_piece, x, y) in square.valid_moves(self.board, self.last_move):
                                circle = pygame.Surface((16, 16), pygame.SRCALPHA)
                                if is_piece:
                                    pygame.draw.circle(circle, (235, 237, 233, 150), (8, 8), 10, 2)
                                else:
                                    pygame.draw.circle(circle, (235, 237, 233, 150), (8, 8), 2)
                                self.board_surface.blit(circle, self.rects[y][x])

                    # Append square to pieces
                    pieces.append(square)

        for piece in pieces:  # draw pieces
            piece.draw(self.board_surface)

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
                # Get hitbox
                rect = self.rects[y][x]
                hitbox = pygame.Rect(
                    rect.x * 4 + 64, rect.y * 4 + 64, 64, 64)

                # Check if rectangle is colliding with mouse's position
                if hitbox.collidepoint(mouse_pos):
                    if self.currently_selected != None:
                        valid_moves = self.currently_selected.valid_moves(self.board, self.last_move)
                        if (0, x, y) in valid_moves or (1, x, y) in valid_moves or (2, x, y) in valid_moves:  # moving and taking pieces
                            if self.move_number == 0 and self.currently_selected.color == "w" or (  # first move or selected piece is not equal to last move's color
                                    self.currently_selected.color != self.last_move["color"]):

                                # Get currently selected position
                                py = self.currently_selected.row  # previous x
                                px = self.currently_selected.col  # previous y

                                # If Pawn, update its "first move" variable
                                if isinstance(self.currently_selected, Pawn):
                                    self.currently_selected.first_move = False

                                # Update last move
                                self.last_move = {
                                    "color": self.currently_selected.color,
                                    "piece": type(self.currently_selected),
                                    "from": (py, px),
                                    "current": (y, x)
                                }

                                # Update move number
                                if self.currently_selected.color == "w":
                                    self.move_number += 1

                                # Update board
                                self.board[py][px] = 0
                                self.board[y][x] = self.currently_selected
                                # Update board when en passant
                                for valid_move in valid_moves:
                                    if valid_move[0] == 2:  # en passant
                                        ly, lx = self.last_move["current"]
                                        offset = 1 if self.last_move["color"] == "w" else -1
                                        self.board[ly + offset][lx] = 0
                                        break

                                # Update piece
                                self.currently_selected.move(y, x)
                                self.currently_selected = None

                    elif square != 0:  # if not an empty square
                        square.is_selected = True
                        self.previously_selected = square
                        self.currently_selected = square

                    else:  # empty square
                        self.currently_selected = None

                    break
