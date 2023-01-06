from utils import separate_sets_from_yaxis, clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "..", "resources", "game"
        )
    )

white_spriteset, black_spriteset = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/pieces.png"))


class Piece:
    rects = [[pygame.Rect(x, y, 16, 16) for x in range(0, 16*8, 16)] for y in range(0, 16*8, 16)]
    images = {
        "w": clip_set_to_list_on_xaxis(white_spriteset),  # white
        "b": clip_set_to_list_on_xaxis(black_spriteset)  # black
    }

    def __init__(self, row, col, color):
        # Position
        self.row = row
        self.col = col
        self.rect = self.rects[self.row][self.col]

        # Color
        self.color = color

        # Attachments
        self.attachments = clip_set_to_list_on_xaxis(
            pygame.image.load(f"{resources_path}/piece_attachments.png"))

        # Status
        self.is_selected = False

    def draw(self, surface, valid_moves):
        # Draw "selected" attachment
        if self.is_selected:
            # Draw attachment
            bkg = pygame.Surface((16, 16), pygame.SRCALPHA)
            bkg.fill((164, 221, 219, 128))
            surface.blit(bkg, self.rect)
            surface.blit(self.attachments, self.rect)

            # Draw valid moves
            for (x, y) in valid_moves:
                circle = pygame.Surface((16, 16), pygame.SRCALPHA)
                pygame.draw.circle(circle, (235, 237, 233, 150), (8, 8), 2)
                surface.blit(circle, self.rects[y][x])

        # Draw piece
        pos = (self.rect.x + self.offset[0], self.rect.y + self.offset[1])
        surface.blit(self.image, pos)

    def move(self, row, col):
        # Position
        self.row = row
        self.col = col
        self.rect = self.rects[self.row][self.col]
