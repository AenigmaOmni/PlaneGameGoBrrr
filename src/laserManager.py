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

    def update(self, delta):
        #update lasers
        for laser in self.playerLasers:
            laser.update(delta, False, True)

        #remove lasers that have gone offscreen
        alive = []
        for laser in self.playerLasers:
            if laser.y > -50:
                alive.append(laser)

        self.playerLasers = alive

    def render(self, surface):
        for laser in self.playerLasers:
            laser.render(surface)