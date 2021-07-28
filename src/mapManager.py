from src.globals import *
from src.map import Map

class MapManager:
    def __init__(self):
        self.speed = BG_SPEED
        self.map1 = None
        self.map2 = None

    def load(self):
        self.map1 = Map("res/bg_1.tmx")
        self.map1.load()
        self.map2 = Map("res/bg_1.tmx")
        self.map2.load()
        self.map2.y = self.map1.y - self.map2.pixel_height

    def update(self, delta):
        self.map1.y = self.map1.y + 1 * self.speed * delta
        self.map2.y = self.map2.y + 1 * self.speed * delta
        if self.map1.y > WINDOW_HEIGHT:
            self.map1.y = self.map2.y - self.map1.pixel_height
        if self.map2.y > WINDOW_HEIGHT:
            self.map2.y = self.map1.y - self.map2.pixel_height

    def render(self, surface):
        self.map1.render(surface)
        self.map2.render(surface)