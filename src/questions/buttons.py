from utils import clip_set_to_list_on_yaxis, separate_sets_from_yaxis, palette_swap
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "questions"
        )
    )

spritesets = separate_sets_from_yaxis(
    pygame.image.load(f"{resources_path}/buttons.png"), (255, 0, 0))


class PlayVsWhoButtons:
    # Initialize
    def __init__(self, enlarge):
        # Images
        order = ["white", "random", "black"]
        images = clip_set_to_list_on_yaxis(spritesets[0])
        
        # Palette
        hover_palette = {
            (173, 119, 87): (77, 43, 50),
            (192, 148, 115): (122, 72, 65),
            (215, 181, 148): (173, 119, 87)
        }

        # Positions
        positions = {
            "white": (100, 56),
            "random": (142, 56),
            "black": (184, 56)
        }

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Initialize
            hover_img = palette_swap(img.convert(), hover_palette)
            img_rect = pygame.Rect(positions[name], img.get_rect().size)
            hitbox = pygame.Rect(
                img_rect.x * enlarge, img_rect.y * enlarge,
                img_rect.width * 2 * enlarge, img_rect.height * 2 * enlarge)
            
            # Resize
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)
            hover_img = pygame.transform.scale(hover_img, size)

            # Append
            button = [
                False,  # is hovered
                img,  # orig image
                hover_img,  # hover image
                img_rect,  # image rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw
    def draw(self, display):
        for button in self.buttons.values():
            is_hovered, orig_img, hover_img, img_rect, _ = button
            img = hover_img if is_hovered else orig_img

            display.blit(img, img_rect)
