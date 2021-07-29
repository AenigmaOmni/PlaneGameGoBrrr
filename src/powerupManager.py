import random
from src.globals import WINDOW_WIDTH
from src.powerup import Powerup

class PowerupManager:
    def __init__(self):
        self.powerups = []
        self.maxScoreSpawn = 900
        self.minScoreSpawn = 400
        self.maxScoreMod = 1.5
        self.scoreToSpawn = random.randint(self.minScoreSpawn, self.maxScoreSpawn)
        self.maxScoreSpawn = self.maxScoreSpawn * self.maxScoreMod

    def spawn(self):
        c = random.randint(1, 2)
        x = random.randint(32, WINDOW_WIDTH - 32)
        y = 0 - 32
        p = Powerup(x, y)
        if c == 1:
            p.type = 1
            p.vFrame = 0
            p.hFrame = 0
        else:
            p.type = 2
            p.vFrame = 0
            p.hFrame = 1
        p.load()
        p.scale()
        self.powerups.append(p)
        self.scoreToSpawn = random.randint(self.minScoreSpawn, self.maxScoreSpawn)
        self.maxScoreSpawn = self.maxScoreSpawn * self.maxScoreMod

    def update(self, delta, player):
        if player.score >= self.scoreToSpawn:
            self.spawn()
        for p in self.powerups:
            p.update(delta, False, True)
            if p.rect.colliderect(player.rect):
                if not p.claimed:
                    p.alive = False
                    p.claimed = True
                    player.applyPowerup(p)

        alive = []
        for p in self.powerups:
            if p.alive:
                alive.append(p)

        self.powerups = alive

    def render(self, surface):
        for p in self.powerups:
            p.render(surface)
