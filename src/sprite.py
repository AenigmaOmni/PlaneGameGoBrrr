import pygame

from src.spatial import Spatial
from src.globals import *

class Sprite(Spatial):
    def __init__(self, imgPath):
        super().__init__()
        self.image = pygame.image.load(imgPath)
        self.vFrame = 0
        self.hFrame = 0

    def scale(self, s):
        backBuffer = pygame.Surface((PLANE_SIZE, PLANE_SIZE))
        backBuffer.blit(self.image, (0,0), pygame.Rect(self.hFrame * PLANE_SIZE, self.vFrame * PLANE_SIZE, PLANE_SIZE, PLANE_SIZE))
        self.image = pygame.transform.scale(backBuffer, (PLANE_SIZE * s, PLANE_SIZE * s))

    def update(self, delta):
        super().update(delta)

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))