from src.mapManager import MapManager
from src.sprite import Sprite
from src.inputMap import InputMap
from src.globals import *
from src.map import Map
from src.player import Player

class World:
    def __init__(self):
        pass

    def init(self):
        self.player = Player()
        self.mapManager = MapManager()
        self.mapManager.load()

    def update(self, delta, inputMap):
        self.mapManager.update(delta)
        self.player.update(delta, inputMap)

    def render(self, surface):
        self.mapManager.render(surface)
        self.player.render(surface)