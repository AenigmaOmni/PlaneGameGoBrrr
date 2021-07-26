from src.laser import Laser

class LaserManager:
    def __init__(self):
        self.playerLasers = []
        self.enemyLasers = []

    def playerFire(self, x, y):
        laser = Laser(x, y)
        self.playerLasers.append(laser)
    
    def enemyFIre(self):
        #self.enemyLasers.append(laser)
        pass

    def update(self, delta):
        for laser in self.playerLasers:
            laser.update(delta)