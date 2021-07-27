from src.laser import Laser

class LaserManager:
    def __init__(self):
        self.playerLasers = []
        self.enemyLasers = []

    def playerFire(self, x, y):
        laser = Laser(x, y)
        laser.load()
        laser.scale()
        self.playerLasers.append(laser)
    
    def enemyFIre(self):
        #self.enemyLasers.append(laser)
        pass

    def update(self, delta, player, enemies):
        #update lasers
        for laser in self.playerLasers:
            laser.update(delta, False, True)

        #remove lasers that have gone offscreen
        alive = []
        for laser in self.playerLasers:
            if laser.y > -50 and laser.alive:
                alive.append(laser)

        self.playerLasers = alive

        #check player laser collision with enemies
        for bullet in self.playerLasers:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.alive = False
                    bullet.alive = False
        #check player collision with enemy lasers
        for bullet in self.enemyLasers:
            if bullet.rect.colliderect(player.rect):
                bullet.alive = False
                player.alive = False

    def render(self, surface):
        for laser in self.playerLasers:
            laser.render(surface)