from pygame.locals import *
import pygame

from src.spatial import Spatial
from src.globals import *

class Sprite(Spatial):
    def __init__(self, imgPath, size):
        super().__init__(size)
        self.vFrame = 0
        self.hFrame = 0
        self.img_path = imgPath
        self.tintSurface = None
        self.tinted = None
        self.doTint = False
        self.mask = None

    def load_tint_surface(self):
        self.mask = pygame.mask.from_surface(self.image, 127)
        self.mask = self.mask.to_surface(unsetcolor=(0, 0, 0, 0))
        self.tintSurface = pygame.Surface((self.real_pixel_size, self.real_pixel_size)).convert_alpha()
        self.tintSurface.set_alpha(200)
        self.tintSurface.fill((255, 255, 255))

    def apply_tint(self):
        self.tinted = self.image.copy()
        self.tinted.blit(self.tintSurface, (0,0))
        self.tinted.blit(self.mask, (0,0), special_flags=pygame.BLEND_RGBA_MULT)

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
        if self.doTint:
            surface.blit(self.tinted, (self.x, self.y))
        else:
            surface.blit(self.image, (self.x, self.y))