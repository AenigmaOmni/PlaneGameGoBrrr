from src.sprite import Sprite
import pygame

class Explosion(Sprite):
    def __init__(self, x, y):
        super().__init__("res/explosion.png", 32)
        self.sound = pygame.mixer.Sound("res/explosion.wav")
        self.timer = 0
        self.delay = 0.08
        self.frame = 0
        self.maxFrame = 8
        self.alive = True
        self.x = x
        self.y = y

    def load(self):
        self.image = pygame.image.load("res/explosion.png")
        self.real_pixel_size = 128
        self.real_pixel_size = 128
        pygame.mixer.Sound.play(self.sound)

    def update(self, delta, doClamp):
        super().update(delta, doClamp, False)
        self.timer += delta
        if self.timer >= self.delay:
            self.timer = 0
            self.frame += 1
            if self.frame == self.maxFrame:
                self.alive = False
                pygame.mixer.Sound.stop(self.sound)


    def render(self, surface):
        offset = 32
        crop = pygame.Rect(self.frame * self.real_pixel_size, 0, self.real_pixel_size, self.real_pixel_size)
        surface.blit(self.image, (self.x - offset,self.y-offset), crop)
        