import pygame

from src.spatial import Spatial
from src.globals import *

class Sprite(Spatial):
    def __init__(self, imgPath):
        super().__init__()
        self.vFrame = 0
        self.hFrame = 0
        self.image = pygame.image.load(imgPath).convert_alpha()
        crop = pygame.Rect(self.hFrame * PLANE_SIZE, self.vFrame * PLANE_SIZE, PLANE_SIZE, PLANE_SIZE)
        self.image = self.image.subsurface(crop)

    def scale(self):
        self.image = pygame.transform.scale(self.image, (PLANE_SIZE * SCALE_FACTOR, PLANE_SIZE * SCALE_FACTOR))

    def update(self, delta):
        super().update(delta)

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))