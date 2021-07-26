class LaserManager:
    def __init__(self):
        self.playerLasers = []
        self.enemyLasers = []

    def playerFire(self, laser):
        self.playerLasers.append(laser)

    def enemyFIre(self, laser):
        self.enemyLasers.append(laser)