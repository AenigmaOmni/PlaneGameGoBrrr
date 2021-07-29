from src.sprite import Sprite
from src.globals import *
import pygame

class Laser(Sprite):
    def __init__(self, x, y, power):
        super().__init__("res/bullets_and_fx.png", BULLET_SIZE)
        self.x = x
        self.y = y
        self.speed = 600
        self.move_y = -1
        self.alive = True
        self.sound = pygame.mixer.Sound("res/gun.wav")
        pygame.mixer.Sound.play(self.sound)
        self.soundDelay = 0.3
        self.soundTimer = 0
        if power == 2:
            self.speed = 700
            self.hFrame = 1
            self.vFrame = 0
        elif power == 3:
            self.damage = 2
            self.hFrame = 0
            self.vFrame = 0
        elif power == 4:
            self.speed = 800
            self.hFrame = 1
            self.vFrame = 0
        elif power == 5:
            self.damage = 3
            self.hFrame = 2
            self.vFrame = 0
        elif power == 6:
            self.hFrame = 3
            self.vFrame = 0
        elif power == 7:
            self.hFrame = 4
            self.vFrame = 0

    def update(self, delta, doClamp, Cont):
        super().update(delta, doClamp, Cont)
        self.soundTimer += delta
        if self.soundTimer >= self.soundDelay:
            pygame.mixer.Sound.stop(self.sound )