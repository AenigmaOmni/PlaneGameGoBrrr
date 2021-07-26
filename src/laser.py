from src.sprite import Sprite
from src.globals import *

class Laser(Sprite):
    def __init__(self, x, y):
        super().__init__("res/bullets_and_fx.png", BULLET_SIZE)
        self.x = x
        self.y = y
        self.speed = 700
        self.move_y = -1