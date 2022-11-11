from utils import clip_set_to_list_on_yaxis
import pygame
import os

pygame.init()
resources_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), 
        "..", "..", "resources", "questions"
        )
    )


class Titles:
    def __init__(self):
        images = clip_set_to_list_on_yaxis(
            pygame.image.load(f"{resources_path}/titles.png"))
        rects = [(105, 36), (112, 118), (96, 192)]
        
        self.titles = []
        for img, rect in zip(images, rects):
            # Resize image
            wd, ht = img.get_size()
            size = (wd * 2, ht * 2)
            img = pygame.transform.scale(img, size)

            # Append
            self.titles.append((img, rect))

    def draw(self, display):
        for image, rect in self.titles:
            display.blit(image, rect)