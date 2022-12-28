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
    images = {
        "w": clip_set_to_list_on_xaxis(white_spriteset),  # white
        "b": clip_set_to_list_on_xaxis(black_spriteset)  # black
    }

    def __init__(self, row, col, color):
        # Position
        self.row = row
        self.col = col

        # Color
        self.color = color

        # Attachments
        self.attachments = clip_set_to_list_on_xaxis(
            pygame.image.load(f"{resources_path}/piece_attachments.png"))

        # Status
        self.is_selected = False

    def draw(self, surface, rect):
        # Draw "selected" attachment
        if self.is_selected:
            # Draw
            bkg = pygame.Surface((16, 16), pygame.SRCALPHA)
            bkg.fill((164, 221, 219, 128))
            surface.blit(bkg, rect)
                        
            surface.blit(self.attachments, rect)

        # Draw piece
        pos = (rect.x + self.offset[0], rect.y + self.offset[1])
        surface.blit(self.image, pos)
