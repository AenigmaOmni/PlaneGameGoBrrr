from src.sprite import Sprite
from src.globals import *

class World:
    def __init__(self):
        pass

    def init(self):
        self.player = Sprite("res/ships_packed.png")
        self.player.hFrame = 0
        self.player.vFrame = 0
        self.player.x = WINDOW_WIDTH / 2 - REAL_PLANE_SIZE / 2
        self.player.y = WINDOW_HEIGHT - REAL_PLANE_SIZE - 20
        self.player.scale(SCALE_FACTOR)

    def update(self, delta):
        pass

    def render(self, surface):
        self.player.render(surface)