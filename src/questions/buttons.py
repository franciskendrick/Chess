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


class PlayAsButtons:
    # Initialize
    def __init__(self, enlarge):
        # Images
        order = ["white", "random", "black"]
        images = clip_set_to_list_on_yaxis(spritesets[0])
        
        # Palette
        hover_palette = {
            (173, 119, 87): (122, 72, 65),
            (192, 148, 115): (173, 119, 87),
            (215, 181, 148): (192, 148, 115)
        }
        selected_palette = {
            "default": {
                (173, 119, 87): (79, 143, 186),
                (192, 148, 115): (115, 190, 211),
                (215, 181, 148): (164, 221, 219)},
            "hover": {
                (173, 119, 87): (60, 94, 139),
                (192, 148, 115): (79, 143, 186),
                (215, 181, 148): (115, 190, 211)}
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
            default_selected_img = palette_swap(img.convert(), selected_palette["default"])
            hover_selected_img = palette_swap(img.convert(), selected_palette["hover"])
            img_rect = pygame.Rect(positions[name], img.get_rect().size)
            hitbox = pygame.Rect(
                img_rect.x * enlarge, img_rect.y * enlarge,
                img_rect.width * 2 * enlarge, img_rect.height * 2 * enlarge)
            
            # Resize
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)
            hover_img = pygame.transform.scale(hover_img, size)
            default_selected_img = pygame.transform.scale(default_selected_img, size)
            hover_selected_img = pygame.transform.scale(hover_selected_img, size)

            # Append
            button = [
                False,  # is hovered
                False,  # toggle status
                img,  # orig image
                hover_img,  # hover image
                default_selected_img,  # default selected image
                hover_selected_img,  # hover selecte image
                img_rect,  # image rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw
    def draw(self, display):
        for button in self.buttons.values():
            is_hovered, toggle_status, orig_img, hover_img, default_selected_img, hover_selected_img, img_rect, _ = button
            
            # Get palette swappend image
            if not toggle_status and is_hovered:
                img = hover_img
            elif toggle_status and is_hovered:
                img = hover_selected_img
            elif toggle_status:
                img = default_selected_img
            else:
                img = orig_img

            # Blit to display
            display.blit(img, img_rect)

    # Action detection
    def button_down_detection(self):
        for (name, button) in self.buttons.items():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            if hitbox.collidepoint(mouse_pos):
                # Update all buttons' toggle status to false
                for button in self.buttons.values():
                    button[1] = False  # toggle status
                
                # Update clicked button's toggle status to true
                self.buttons[name][1] = True  # toggle status

                # Break loop
                break

    def button_over_detection(self):
        for button in self.buttons.values():
            *_, hitbox = button
            
            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions
    def reset_overdetection(self):
        for button in self.buttons.values():
            button[0] = False


class PlayVsButtons:
    # Initialize
    def __init__(self, enlarge):
        # Images
        order = ["easy", "medium", "hard"]
        images = clip_set_to_list_on_yaxis(spritesets[1])

        # Palette
        hover_palette = {
            (173, 119, 87): (122, 72, 65),
            (192, 148, 115): (173, 119, 87),
            (215, 181, 148): (192, 148, 115)
        }
        selected_palette = {
            "default": {
                (173, 119, 87): (79, 143, 186),
                (192, 148, 115): (115, 190, 211),
                (215, 181, 148): (164, 221, 219)},
            "hover": {
                (173, 119, 87): (60, 94, 139),
                (192, 148, 115): (79, 143, 186),
                (215, 181, 148): (115, 190, 211)}
        }

        # Positions
        positions = {
            "easy": (37, 138),
            "medium": (121, 138),
            "hard": (205, 138)
        }

        # Buttons
        self.buttons = {}
        for name, img in zip(order, images):
            # Initialize
            hover_img = palette_swap(img.convert(), hover_palette)
            default_selected_img = palette_swap(img.convert(), selected_palette["default"])
            hover_selected_img = palette_swap(img.convert(), selected_palette["hover"])
            img_rect = pygame.Rect(positions[name], img.get_rect().size)
            hitbox = pygame.Rect(
                img_rect.x * enlarge, img_rect.y * enlarge,
                img_rect.width * 2 * enlarge, img_rect.height * 2 * enlarge)
            
            # Resize
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)
            hover_img = pygame.transform.scale(hover_img, size)
            default_selected_img = pygame.transform.scale(default_selected_img, size)
            hover_selected_img = pygame.transform.scale(hover_selected_img, size)

            # Append
            button = [
                False,  # is hovered
                False,  # toggle status
                img,  # orig image
                hover_img,  # hover image
                default_selected_img,  # default selected image
                hover_selected_img,  # hover selecte image
                img_rect,  # image rectangle
                hitbox  # hitbox
            ]
            self.buttons[name] = button

    # Draw
    def draw(self, display):
        for button in self.buttons.values():
            is_hovered, toggle_status, orig_img, hover_img, default_selected_img, hover_selected_img, img_rect, _ = button
            
            # Get palette swappend image
            if not toggle_status and is_hovered:
                img = hover_img
            elif toggle_status and is_hovered:
                img = hover_selected_img
            elif toggle_status:
                img = default_selected_img
            else:
                img = orig_img

            # Blit to display
            display.blit(img, img_rect)

    # Action detection
    def button_down_detection(self):
        for (name, button) in self.buttons.items():
            *_, hitbox = button

            mouse_pos = pygame.mouse.get_pos()
            if hitbox.collidepoint(mouse_pos):
                # Update all buttons' toggle status to false
                for button in self.buttons.values():
                    button[1] = False  # toggle status
                
                # Update clicked button's toggle status to true
                self.buttons[name][1] = True  # toggle status

                # Break loop
                break

    def button_over_detection(self):
        for button in self.buttons.values():
            *_, hitbox = button
            
            mouse_pos = pygame.mouse.get_pos()
            button[0] = True if hitbox.collidepoint(mouse_pos) else False

    # Functions
    def reset_overdetection(self):
        for button in self.buttons.values():
            button[0] = False
