from src.sprite import Sprite
from src.globals import *

class Player(Sprite):
    def __init__(self, lm):
        super().__init__("res/ships_packed.png", PLANE_SIZE)
        self.hFrame = 0
        self.vFrame = 0
        self.x = WINDOW_WIDTH / 2 - REAL_PLANE_SIZE / 2
        self.y = WINDOW_HEIGHT - REAL_PLANE_SIZE - 20

        self.laserManager = lm

        self.canFire = True
        self.fireTimer = 0
        self.fireDelay = 0.2
        self.damage = 1
        self.hp = 10
        self.alive = True

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False

    def load(self):
        super().load()
        self.scale()

    def update(self, delta, doClamp, inputMap, world):
        if inputMap.w == True:
            self.move_y = -1
        elif inputMap.s == True:
            self.move_y = 1
        if inputMap.a == True:
            self.move_x = -1
        elif inputMap.d == True:
            self.move_x = 1

        super().update(delta, doClamp, False)

        if inputMap.space == True:
            if self.canFire:
                self.canFire = False
                self.laserManager.playerFire(self.x + self.size / 2, self.y)

        if not self.canFire:
            self.fireTimer += delta
            if self.fireTimer >= self.fireDelay:
                self.fireTimer = 0
                self.canFire = True

        if not self.alive:
            world.game_over = True