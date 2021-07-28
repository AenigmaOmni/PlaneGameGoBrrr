from src.explosion import Explosion

class ExplosionManager:
    def __init__(self):
        self.explosions = []

    def spawnExplosion(self, x, y):
        explosion = Explosion(x, y)
        explosion.load()
        self.explosions.append(explosion)

    def update(self, delta):
        for e in self.explosions:
            e.update(delta, False)


    def render(self, surface):
        for e in self.explosions:
            e.render(surface)