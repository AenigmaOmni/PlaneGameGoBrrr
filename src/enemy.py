from src.globals import PLANE_SIZE
from src.sprite import Sprite


class Enemy(Sprite):
    def __init__(self):
        self.alive = True
        super().__init__("res/ships_packed.png", PLANE_SIZE)
        self.hFrame = 2
        self.vFrame = 0

        self.canFire = True
        self.fireTimer = 0
        self.fireDelay = 0.1

        self.hp = 1

    def takeDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.alive = False