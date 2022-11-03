import pygame

pygame.init()


class Window:
    rect = pygame.Rect(0, 0, 640, 640)
    enlarge = (pygame.display.Info().current_h - 80) / rect.height
    win_size = (int(rect.width * enlarge), int(rect.height * enlarge))


window = Window()
