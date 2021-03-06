from src.sprite import Sprite
from src.globals import *
import pygame

class EnemyBullet(Sprite):

    def __init__(self, x, y, damage):
        super().__init__("res/bullets_and_fx.png", BULLET_SIZE)
        self.x = x
        self.y = y
        self.damage = damage
        self.speed = 400
        self.move_y = 1
        self.alive = True
        self.hFrame = 2

    def load(self):
        super().load()
        self.image = pygame.transform.flip(self.image, 0, 1)