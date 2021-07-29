from src.powerupManager import PowerupManager
from src.laserManager import LaserManager
from src.mapManager import MapManager
from src.sprite import Sprite
from src.inputMap import InputMap
from src.globals import *
from src.map import Map
from src.player import Player
from src.enemyManager import EnemyManager
from src.hudManager import HudManager
import pygame
from pygame.locals import *

class World:

    def init(self):
        self.game_over = False
        self.load_menu()
        self.delay_menu = False
        self.delay_gameover = False
        self.delay_play = False
        self.menu_delay = 1
        self.gameover_delay = 1
        self.menu_timer = 0
        self.gameover_timer = 0
        self.play_delay = 0.2
        self.play_timer = 0

    def load_menu(self):
        self.state = MENU_STATE
        self.menu_background = pygame.image.load("res/cover.png")
        self.menu_font = pygame.font.SysFont(None, 110)
        self.menu_text = self.menu_font.render("Plane Game Go Brrr", True, (255, 255, 255))    
        self.continue_font = pygame.font.SysFont(None, 60)
        self.continue_text = self.continue_font.render("Press Space to Play", True, (255, 255, 255))
        self.delay_menu = True

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
        self.delay_gameover = True

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
        self.hudManager = None
        self.powerupManager = None

    def load_play(self):
        self.state = PLAY_STATE
        self.laserManager = LaserManager()
        self.enemyManager = EnemyManager(self.laserManager)
        self.player = Player(self.laserManager)
        self.player.load()
        self.hudManager = HudManager()
        self.hudManager.load(self.player)
        self.mapManager = MapManager()
        self.mapManager.load()
        self.enemyManager.spawn(2)
        self.powerupManager = PowerupManager()
        self.delay_play = True
        self.bg_music = pygame.mixer.music.load("res/My-Story.ogg")
        pygame.mixer.music.play(-1)

    def play_update(self, delta, inputMap):
        if self.delay_play:
            self.play_timer += delta
            if self.play_timer >= self.play_delay:
                self.play_timer = 0
                self.delay_play = False
        if self.delay_play == False:
            self.mapManager.update(delta)
            self.player.update(delta, True, inputMap, self)
            self.laserManager.update(delta, self.player, self.enemyManager.enemies)
            self.enemyManager.update(delta, self.player)
            self.hudManager.update(self.player)
            self.powerupManager.update(delta, self.player)

    def menu_update(self, delta, inputMap):
        if self.delay_menu:
            self.menu_timer += delta
            if self.menu_timer >= self.menu_delay:
                self.delay_menu = False
                self.menu_timer = 0
        if inputMap.space and self.delay_menu == False:
            self.unload_menu()
            self.load_play()

    def menu_render(self, surface):
        surface.blit(self.menu_background, (0,0))
        surface.blit(self.menu_text, (WINDOW_WIDTH / 2 - self.menu_text.get_size()[0] / 2, WINDOW_HEIGHT / 2 - 100))
        surface.blit(self.continue_text, (WINDOW_WIDTH / 2 - self.continue_text.get_size()[0] / 2, WINDOW_HEIGHT / 2))       

    def gameover_update(self, delta, inputMap):
        if self.delay_gameover:
            self.gameover_timer += delta
            if self.gameover_timer >= delta:
                self.delay_gameover = False
                self.gameover_timer = 0
        if inputMap.space == True and self.delay_gameover == False:
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
        self.hudManager.render(surface)
        self.powerupManager.render(surface)

    def update(self, delta, inputMap):
        if self.state == MENU_STATE:
            self.menu_update(delta, inputMap)
        elif self.state == PLAY_STATE:
            self.play_update(delta, inputMap)
        elif self.state == GAMEOVER_STATE:
            self.gameover_update(delta, inputMap)

        if self.game_over:
            self.unload_play()
            self.load_gameover()
            self.game_over = False

    def render(self, surface):
        if self.state == MENU_STATE:
            self.menu_render(surface)

        elif self.state == PLAY_STATE:
            self.play_render(surface)
        
        elif self.state == GAMEOVER_STATE:
            self.gameover_render(surface)