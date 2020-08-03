import pygame
from Pacman.Point import *
START = (0, 0)


class Pacman(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.position = Point(START[0], START[1])
        self.image = None

    def move(self, key):
        pass