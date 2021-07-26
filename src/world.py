from src.mapManager import MapManager
from src.sprite import Sprite
from src.inputMap import InputMap
from src.globals import *
from src.map import Map

class World:
    def __init__(self):
        pass

    def init(self):
        self.player = Sprite("res/ships_packed.png")
        self.player.hFrame = 0
        self.player.vFrame = 0
        self.player.x = WINDOW_WIDTH / 2 - REAL_PLANE_SIZE / 2
        self.player.y = WINDOW_HEIGHT - REAL_PLANE_SIZE - 20
        self.player.scale()
        self.mapManager = MapManager()
        self.mapManager.load()

    def update(self, delta, inputMap):
        if inputMap.w == True:
            self.player.move_y = -1
        elif inputMap.s == True:
            self.player.move_y = 1
        if inputMap.a == True:
            self.player.move_x = -1
        elif inputMap.d == True:
            self.player.move_x = 1

        self.mapManager.update(delta)
        self.player.update(delta)

    def render(self, surface):
        self.mapManager.render(surface)
        self.player.render(surface)