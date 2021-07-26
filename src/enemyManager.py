from src.globals import *
from src.enemy import Enemy
from random import *

class EnemyManager:
    def __init__(self, lm):
        self.laserManager = lm
        self.spawnDelay = 3
        self.maxSpawns = 4
        self.spawnTimer = 0
    
        self.enemies = []

    def spawn(self, count):
        for i in range(0, count):
            e = Enemy()
            e.load()
            e.scale()
            e.x = randint(16, WINDOW_WIDTH - PLANE_SIZE)
            e.y = -REAL_PLANE_SIZE
            e.move_y = 1
            e.speed = 100
            self.enemies.append(e)

    def update_enemies(self, delta):
        for enemy in self.enemies:
            enemy.update(delta, False, True)

    def remove_dead(self):
        alive = []
        for enemy in self.enemies:
            if enemy.y < WINDOW_HEIGHT and enemy.alive == True:
                alive.append(enemy)
        self.enemies = alive

    def update(self, delta):
        self.spawnTimer += delta
        if self.spawnTimer > self.spawnDelay:
            self.spawn(randint(1, self.maxSpawns))
            self.spawnTimer = 0

        self.update_enemies(delta)
        self.remove_dead()

    def render(self, surface):
        for enemy in self.enemies:
            enemy.render(surface)