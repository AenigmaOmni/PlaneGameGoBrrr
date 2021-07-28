from src.globals import WINDOW_HEIGHT
from src.explosionManager import ExplosionManager
from src.laser import Laser
from src.explosionManager import ExplosionManager
import pygame
from src.enemyBullet import EnemyBullet

class LaserManager:
    def __init__(self):
        self.em = ExplosionManager()
        self.playerLasers = []
        self.enemyLasers = []

    def playerFire(self, x, y):
        laser = Laser(x, y)
        laser.load()
        laser.scale()
        self.playerLasers.append(laser)
    
    def enemyFire(self, x, y ,damage, v, h):
        b = EnemyBullet(x, y, damage)
        b.vFrame = v
        b.hFrame = h
        b.load()
        b.scale()
        self.enemyLasers.append(b)

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

        #update enemy bullets
        for bullet in self.enemyLasers:
            bullet.update(delta, False, True)

        #remove enemy that have gone offscreen
        alive = []
        for bullet in self.enemyLasers:
            if bullet.y < WINDOW_HEIGHT and bullet.alive:
                alive.append(bullet)

        self.enemyLasers = alive  

        #check player laser collision with enemies
        for bullet in self.playerLasers:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    if not enemy.takeDamage(player.damage):
                        self.em.spawnExplosion(enemy.x, enemy.y)
                    bullet.alive = False

        #check player collision with enemy lasers
        for bullet in self.enemyLasers:
            if bullet.rect.colliderect(player.rect):
                bullet.alive = False
                player.takeDamage(bullet.damage)

        #update explosion manager
        self.em.update(delta)

    def render(self, surface):
        for laser in self.playerLasers:
            laser.render(surface)

        for bullet in self.enemyLasers:
            bullet.render(surface)

        self.em.render(surface)