from pytmx.util_pygame import load_pygame
import pygame
from src.globals import *

class Map:
    def __init__(self, path):
        self.x = 0
        self.y = 0
        self.tiled_map = load_pygame(path)
        self.width = self.tiled_map.width
        self.height = self.tiled_map.height
        self.pixel_width = self.tiled_map.width * TILE_SIZE
        self.pixel_height = self.tiled_map.height * TILE_SIZE

    def load(self):
        backBuffer = pygame.Surface((480, 480))
        for j in range(0, self.height):
            for i in range(0, self.width):
                tile = self.tiled_map.get_tile_image(i, j, 0)
                if tile != None:
                    backBuffer.blit(tile, (i * TILE_SIZE, j * TILE_SIZE))
        self.image = pygame.transform.scale(backBuffer, (self.pixel_width * SCALE_FACTOR, self.pixel_height * SCALE_FACTOR))
        self.pixel_width = self.pixel_width * SCALE_FACTOR
        self.pixel_height = self.pixel_height * SCALE_FACTOR
        self.image.convert()

    def render(self, surface):
        surface.blit(self.image, (self.x, self.y))

        