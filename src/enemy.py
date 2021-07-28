from pygame.display import update
from src.globals import PLANE_SIZE
from src.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, lmanager):
        self.alive = True
        super().__init__("res/ships_packed.png", PLANE_SIZE)
        self.hFrame = 2
        self.vFrame = 0

        self.fireTimer = 3
        self.fireDelay = 4

        self.blinkTimer = 0
        self.blinkDelay = 0.1

        self.hp = 1
        self.damage = 1

        self.laserManager = lmanager

    def fire(self):
        self.laserManager.enemyFire(self.x + self.size / 2, self.y, self.damage)

    def takeDamage(self, damage):
        self.doTint = True
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False
            return False
        return True

    def update(self, delta, doClamp, inputMap):
        super().update(delta, doClamp, inputMap)
        if self.doTint:
            self.blinkTimer += delta
            if self.blinkTimer >= self.blinkDelay:
                self.blinkTimer = 0
                self.doTint = False

        self.fireTimer += delta
        if self.fireTimer >= self.fireDelay:
            self.fireTimer = 0
            self.fire()