from utils import separate_sets_from_xaxis, clip_set_to_list_on_xaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "game"
        )
    )


class Profiles:
    def __init__(self):
        # Images
        order = ["you", "alexander"]
        spritesets = separate_sets_from_xaxis(
            pygame.image.load(f"{resources_path}/player_profiles.png"), (255, 0, 0))
        images = {
            "you": clip_set_to_list_on_xaxis(spritesets[0]),
            "alexander": clip_set_to_list_on_xaxis(spritesets[1])
        }

        # Positions
        positions = {
            "you": [[60, 588], [114, 588]],
            "alexander": [[60, 4], [114, 4]]
        }

        # Profiles
        self.profiles = {}
        for name in order:
            # Initialize
            icon_img, name_img = images[name]
            icon_pos, name_pos = positions[name]

            # Resize icon
            wd, ht = icon_img.get_size()
            size = (wd * 3, ht * 3)
            icon_img = pygame.transform.scale(icon_img, size)
            
            # Resize name
            wd, ht = name_img.get_size()
            size = (wd * 3, ht * 3)
            name_img = pygame.transform.scale(name_img, size)

            # Append
            profile = [
                icon_img, name_img,
                icon_pos, name_pos
            ]
            self.profiles[name] = profile

    def draw(self, display):
        for profiles in self.profiles.values():
            icon_img, name_img, icon_pos, name_pos = profiles

            # Blit to display
            display.blit(icon_img, icon_pos)
            display.blit(name_img, name_pos)
