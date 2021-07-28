from src.sprite import Sprite
from src.globals import *
import pygame

class Laser(Sprite):
    def __init__(self, x, y):
        super().__init__("res/bullets_and_fx.png", BULLET_SIZE)
        self.x = x
        self.y = y
        self.speed = 700
        self.move_y = -1
        self.alive = True
        self.sound = pygame.mixer.Sound("res/gun.wav")
        pygame.mixer.Sound.play(self.sound)
        self.soundDelay = 0.3
        self.soundTimer = 0


    def update(self, delta, doClamp, Cont):
        super().update(delta, doClamp, Cont)
        self.soundTimer += delta
        if self.soundTimer >= self.soundDelay:
            pygame.mixer.Sound.stop(self.sound )