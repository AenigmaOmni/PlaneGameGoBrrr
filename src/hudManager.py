import pygame
from src.globals import *

class HudManager:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def load(self, player):
        self.bg = pygame.image.load("res/hud_background.png")
        self.hp_font = pygame.font.SysFont(None, 40)
        self.score_font = pygame.font.SysFont(None, 40)
        self.update(player)
    
    def update(self, player):
        self.hp_text = self.hp_font.render("ARMOR: " + str(player.hp) + "/10", True, (255,255,255))
        self.score_text = self.score_font.render("SCORE: " + str(player.score), True, (255,255,255))

    def render(self, surface):
        surface.blit(self.bg, (0,0))
        surface.blit(self.hp_text, (100, 10))
        surface.blit(self.score_text, (WINDOW_WIDTH - 300, 10))