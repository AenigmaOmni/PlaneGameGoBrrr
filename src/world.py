from src.laserManager import LaserManager
from src.mapManager import MapManager
from src.sprite import Sprite
from src.inputMap import InputMap
from src.globals import *
from src.map import Map
from src.player import Player
from src.enemyManager import EnemyManager

class World:
    def __init__(self):
        pass

    def init(self):
        self.laserManager = LaserManager()
        self.enemyManager = EnemyManager(self.laserManager)
        self.player = Player(self.laserManager)
        self.player.load()
        self.mapManager = MapManager()
        self.mapManager.load()

        self.enemyManager.spawn(2)


    def update(self, delta, inputMap):
        self.mapManager.update(delta)
        self.player.update(delta, True, inputMap)
        self.laserManager.update(delta, self.player, self.enemyManager.enemies)
        self.enemyManager.update(delta)

    def render(self, surface):
        self.mapManager.render(surface)
        self.laserManager.render(surface)
        self.enemyManager.render(surface)
        self.player.render(surface)