from src.sprite import Sprite

class Powerup(Sprite):
    def __init__(self, x, y):
        self.size = 16
        self.imgPath = "res/powerups_packed.png"
        super().__init__(self.imgPath, self.size)
        self.move_y = 1
        self.speed = 50
        self.type = 1
        self.alive = True
        self.claimed = False