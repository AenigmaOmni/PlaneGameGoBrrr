import pygame
from src.globals import *

class Spatial:
    def __init__(self, size):
        self.speed = 450
        self.move_x = 0
        self.move_y = 0
        self.x = 0
        self.y = 0
        self.size = size
        self.real_pixel_size = None
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)

    def update(self, delta, doClamp):
        self.x = self.x + (self.move_x * delta * self.speed)
        self.y = self.y + (self.move_y * delta * self.speed)
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        self.move_x = 0
        self.move_y = 0
        if doClamp:
            self.clamp_to_world()
    
    def clamp_to_world(self):
        if self.x < 0:
            self.x = 0
        if self.x > WINDOW_WIDTH - self.real_pixel_size:
            self.x = WINDOW_WIDTH - self.real_pixel_size
        if self.y < 0:
            self.y = 0
        if self.y > WINDOW_HEIGHT - self.real_pixel_size:
            self.y = WINDOW_HEIGHT - self.real_pixel_size