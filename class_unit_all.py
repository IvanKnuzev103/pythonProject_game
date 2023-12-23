import pygame
from pygame import K_DOWN, K_UP, K_RIGHT, K_LEFT

import class_all_objects

pygame.init()


class unit(class_all_objects.Object):
    def __init__(self, width, height, screen, *parametrs):
        super().__init__(width, height, screen, *parametrs)


