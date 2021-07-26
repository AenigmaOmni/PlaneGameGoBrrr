import pygame
from src.globals import *

class Spatial:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = PLANE_SIZE
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self, delta):
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)