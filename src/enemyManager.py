from src.globals import *
from src.enemy import Enemy
from random import *

class EnemyManager:
    def __init__(self, lm):
        self.laserManager = lm
        self.spawnDelay = randint(2, 4)
        self.maxSpawns = 4
        self.spawnTimer = 0
    
        self.enemies = []

    def spawnTankObject(self, v, h, hp, d):
        e = Enemy(self.laserManager, "res/tiles_ground.png", TANK_SIZE)
        e.vFrame = v
        e.hFrame = h
        e.damage = d
        e.move_y = 1
        e.speed = BG_SPEED
        e.hp = hp
        e.load()
        e.scale()
        e.x = randint(32, WINDOW_WIDTH - REAL_PLANE_SIZE)
        e.y = -REAL_PLANE_SIZE
        e.load_tint_surface()
        e.apply_tint()
        return e

    def spawnPlaneObject(self, v, h, speed, hp, d):
        e = Enemy(self.laserManager, "res/ships_packed.png", PLANE_SIZE)
        e.vFrame = v
        e.hFrame = h
        e.damage = d
        e.speed = speed
        e.load()
        e.scale()
        e.load_tint_surface()
        e.apply_tint()
        e.x = randint(32, WINDOW_WIDTH - REAL_PLANE_SIZE)
        e.y = -REAL_PLANE_SIZE
        e.move_y = 1
        e.hp = hp
        return e

    def spawnTank(self, color, size):
        if color == "Red":
            if size == "Big":
                e = self.spawnTankObject(0, 1, 4, 1)
                self.enemies.append(e)
            else:
                e = self.spawnTankObject(0, 2, 3, 1)
                self.enemies.append(e)   
        else:
            e = self.spawnTankObject(1, 0, 5, 2)
            self.enemies.append(e)          

    def spawnPlane(self, color, size):
        if color == "Red":
            if size == "Big":
                e = self.spawnPlaneObject(0, 1, 80, 2, 1)
                self.enemies.append(e)

            else: #Red Small
                e = self.spawnPlaneObject(1, 1, 60, 1, 1)
    
        elif color == "Green":
            if size == "Big":
                e = self.spawnPlaneObject(0, 2, 100, 3, 2)
                self.enemies.append(e)

            else: #Green Small
                e = self.spawnPlaneObject(1, 2, 80, 2, 1)
                self.enemies.append(e)
        
        elif color == "Yellow":
            if size == "Big":
                e = self.spawnPlaneObject(0, 3, 110, 4, 2)
                self.enemies.append(e)

            else: #Yellow Small
                e = self.spawnPlaneObject(1, 3, 100, 3, 2)
                self.enemies.append(e)

    def spawn(self, count):
        for i in range(0, count):
            c = randint(1, 4)
            if c == 1:
                s = randint(1, 2)
                if s == 1:
                    self.spawnPlane("Red", "Big")
                else:
                    self.spawnPlane("Red", "Small")
            elif c == 2:
                s = randint(1, 2)
                if s == 1:
                    self.spawnPlane("Green", "Big")
                else:
                    self.spawnPlane("Green", "Small")
            elif c == 3:
                s = randint(1, 2)
                if s == 1:
                    self.spawnPlane("Yellow", "Big")
                else:
                    self.spawnPlane("Yellow", "Small")
            elif c == 4:
                s = randint(1, 3)
                if s == 1:
                    self.spawnTank("Red", "Big")
                elif s == 2:
                    self.spawnTank("Red", "Small")
                else:
                    self.spawnTank("Green", None)

        self.spawnDelay = randint(1, 3)


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