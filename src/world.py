from src.laserManager import LaserManager
from src.mapManager import MapManager
from src.sprite import Sprite
from src.inputMap import InputMap
from src.globals import *
from src.map import Map
from src.player import Player
from src.enemyManager import EnemyManager
import pygame

class World:

    def init(self):
        self.load_menu()

    def load_menu(self):
        self.state = MENU_STATE
        self.menu_font = pygame.font.SysFont(None, 110)
        self.menu_text = self.menu_font.render("Plane Game Go Brrr", True, (255, 255, 255))    
        self.continue_font = pygame.font.SysFont(None, 60)
        self.continue_text = self.continue_font.render("Press Space to Play", True, (255, 255, 255))

    def unload_menu(self):
        self.menu_font = None
        self.menu_text = None
        self.continue_font = None
        self.continue_text = None

    def load_gameover(self):
        self.state = GAMEOVER_STATE
        self.gameover_font = pygame.font.SysFont(None, 140)
        self.gameover_text = self.gameover_font.render("Game Over", True, (255, 255, 255))
        self.continue_font = pygame.font.SysFont(None, 80)
        self.continue_text = self.continue_font.render("Press Space to Continue", True, (255, 255, 255))

    def unload_gameover(self):
        self.gameover_font = None
        self.gameover_text = None
        self.continue_font = None
        self.continue_text = None

    def unload_play(self):
        self.laserManager = None
        self.enemyManager = None
        self.player = None
        self.mapManager = None

    def load_play(self):
        self.state = PLAY_STATE
        self.laserManager = LaserManager()
        self.enemyManager = EnemyManager(self.laserManager)
        self.player = Player(self.laserManager)
        self.player.load()
        self.mapManager = MapManager()
        self.mapManager.load()
        self.enemyManager.spawn(2)

    def play_update(self, delta, inputMap):
        self.mapManager.update(delta)
        self.player.update(delta, True, inputMap)
        self.laserManager.update(delta, self.player, self.enemyManager.enemies)
        self.enemyManager.update(delta)

    def menu_update(self, delta, inputMap):
        if inputMap.space == True:
            self.unload_menu()
            self.load_play()

    def menu_render(self, surface):
        surface.blit(self.menu_text, (WINDOW_WIDTH / 2 - self.menu_text.get_size()[0] / 2, WINDOW_HEIGHT / 2 - 100))
        surface.blit(self.continue_text, (WINDOW_WIDTH / 2 - self.continue_text.get_size()[0] / 2, WINDOW_HEIGHT / 2))       

    def gameover_update(self, delta, inputMap):
        if inputMap.space == True:
            self.unload_gameover()
            self.load_menu()

    def gameover_render(self, surface):
        surface.blit(self.gameover_text, (WINDOW_WIDTH / 2 - self.gameover_text.get_size()[0] / 2, WINDOW_HEIGHT / 2 - 100))
        surface.blit(self.continue_text, (WINDOW_WIDTH / 2 - self.continue_text.get_size()[0] / 2, WINDOW_HEIGHT / 2))

    def play_render(self, surface):
        self.mapManager.render(surface)
        self.laserManager.render(surface)
        self.enemyManager.render(surface)
        self.player.render(surface)

    def update(self, delta, inputMap):
        if self.state == MENU_STATE:
            self.menu_update(delta, inputMap)
        elif self.state == PLAY_STATE:
            self.play_update(delta, inputMap)
        elif self.state == GAMEOVER_STATE:
            self.gameover_update(delta, inputMap)

    def render(self, surface):
        if self.state == MENU_STATE:
            self.menu_render(surface)

        elif self.state == PLAY_STATE:
            self.play_render(surface)
        
        elif self.state == GAMEOVER_STATE:
            self.gameover_render(surface)