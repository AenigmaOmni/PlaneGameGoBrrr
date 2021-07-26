import pygame

from src.spatial import Spatial
from src.globals import *

class Sprite(Spatial):
    def __init__(self, imgPath, size):
        super().__init__(size)
        self.vFrame = 0
        self.hFrame = 0
        self.img_path = imgPath

    def load(self):
        self.image = pygame.image.load(self.img_path).convert_alpha()
        crop = pygame.Rect(self.hFrame * self.size, self.vFrame * self.size, self.size, self.size)
        self.image = self.image.subsurface(crop)

    def scale(self):
        self.image = pygame.transform.scale(self.image, (self.size * SCALE_FACTOR, self.size * SCALE_FACTOR))
        self.real_pixel_size = self.size * SCALE_FACTOR
        
    def update(self, delta, doClamp, cont):
        super().update(delta, doClamp, cont)

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))