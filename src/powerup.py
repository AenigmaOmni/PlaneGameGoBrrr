from src.sprite import Sprite

class Powerup(Sprite):
    def __init__(self, x, y):
        self.imgPath = "res/powerups_packed.png"
        super().__init__(self.imgPath, 16)
        self.x = x
        self.y = y
        self.move_y = 1
        self.speed = 50
        self.type = 1
        self.alive = True
        self.claimed = False