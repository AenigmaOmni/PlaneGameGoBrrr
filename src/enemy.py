from pygame.display import update
from src.globals import PLANE_LETHAL_FIRE, PLANE_NORMAL_FIRE, PLANE_SIZE, TANK_FIRE, TANK_LETHAL_FIRE
from src.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, lmanager, imgPath, size):
        self.alive = True
        super().__init__(imgPath, size)
        self.hFrame = 2
        self.vFrame = 0
        self.fire_type = PLANE_NORMAL_FIRE

        self.fireTimer = 3
        self.fireDelay = 4

        self.blinkTimer = 0
        self.blinkDelay = 0.1

        self.hp = 1
        self.damage = 1
        self.score = 0

        self.laserManager = lmanager

    def fire(self):
        x = self.x + self.size / 2
        y = self.y
        if self.fire_type == PLANE_NORMAL_FIRE:
            self.laserManager.enemyFire(x, y, self.damage, 0, 2)
        elif self.fire_type == PLANE_LETHAL_FIRE:
            self.laserManager.enemyFire(x, y, self.damage, 0, 3)
        elif self.fire_type == TANK_FIRE:
            self.laserManager.enemyFire(x, y, self.damage, 0, 1)
        elif self.fire_type == TANK_LETHAL_FIRE:
            self.laserManager.enemyFire(x, y, self.damage, 0, 5)

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