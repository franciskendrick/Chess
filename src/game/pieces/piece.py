from utils import separate_sets_from_yaxis, clip_set_to_list_on_xaxis, clip_set_to_list_on_yaxis
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
    offsets = [
        (1, 1), (1, 1), (3, 1), (3, 1), (2, 1), (4, 3)
    ]

    def __init__(self, row, col, color):
        # Position
        self.row = row
        self.col = col
        self.rect = self.rects[self.row][self.col]
        
        # Color
        self.color = color

        # Attachments
        self.attachments = clip_set_to_list_on_yaxis(
            pygame.image.load(f"{resources_path}/piece_attachments.png"))

        # Status
        self.is_selected = False
        self.on_promotion = False

    def draw(self, surface):
        # Draw "selected" attachment
        if self.is_selected:
            # Draw attachment
            bkg = pygame.Surface((16, 16), pygame.SRCALPHA)
            bkg.fill((164, 221, 219, 128))
            surface.blit(bkg, self.rect)
            surface.blit(self.attachments[0], self.rect)

        # Draw piece
        pos = (self.rect.x + self.offset[0], self.rect.y + self.offset[1])
        surface.blit(self.image, pos)

        # Draw "promotion" attachment
        if self.on_promotion:
            # Draw board's background
            bkg = pygame.Surface((128, 128), pygame.SRCALPHA)
            bkg.fill((9, 10, 20, 68))
            surface.blit(bkg, (0, 0))

            # Draw buttons
            for button in self.promotion_buttons.values():
                is_hovered, orig_img, hover_img, pos, _  = button
                img = hover_img if is_hovered else orig_img
                surface.blit(img, pos)

            # Draw frame attachment
            pos = (self.rect.x - 2, self.rect.y)
            surface.blit(self.attachments[1], pos)

    def move(self, row, col):
        # Position
        self.row = row
        self.col = col
        self.rect = self.rects[self.row][self.col]
