from src.sprite import Sprite
from src.globals import *

class Player(Sprite):
    def __init__(self):
        super().__init__("res/ships_packed.png", PLANE_SIZE)
        self.hFrame = 0
        self.vFrame = 0
        self.x = WINDOW_WIDTH / 2 - REAL_PLANE_SIZE / 2
        self.y = WINDOW_HEIGHT - REAL_PLANE_SIZE - 20
        self.scale()
        self.real_pixel_size = self.size * SCALE_FACTOR 

    def update(self, delta, inputMap):
        if inputMap.w == True:
            self.move_y = -1
        elif inputMap.s == True:
            self.move_y = 1
        if inputMap.a == True:
            self.move_x = -1
        elif inputMap.d == True:
            self.move_x = 1

        super().update(delta)