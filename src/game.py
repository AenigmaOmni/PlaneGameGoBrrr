import pygame
from src.inputMap import InputMap
from src.world import World
from src.globals import *
from pygame.locals import *

class Game:
    def __init__(self):
        self.running = True
        self.on_init()
        self.lastTime = 0
        self.inputMap = InputMap()
        self.post_init()

    def run(self):
        while self.running:
            self.processEvents()
            self.update()
            self.render()
            self.fpsClock.tick()

    def processEvents(self):
        self.inputMap.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys = pygame.key.get_pressed()
        if keys[K_d]:
            self.inputMap.d = True
        if keys[K_a]:
            self.inputMap.a = True
        if keys[K_s]:
            self.inputMap.s = True
        if keys[K_w]:
            self.inputMap.w = True
        if keys[K_SPACE]:
            self.inputMap.space = True

    def update(self):
        t = pygame.time.get_ticks()
        # deltaTime in seconds.
        delta = (t - self.lastTime) / 1000.0
        self.lastTime = t

        #do updating here
        self.world.update(delta, self.inputMap)
        
        #stop updating

    def render(self):
        self.screen.fill((0,0,0))

        #do rendering here
        self.world.render(self.screen)

        #stop rendering
        #img = self.font.render("FPS: " + str(round(self.fpsClock.get_fps())), True, (255, 255, 255))

        #self.screen.blit(img, (20, 20))

        pygame.display.flip()

    def cleanUp(self):
        pygame.quit()

    def on_init(self):
        pygame.init()
        self.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.screen = pygame.display.set_mode(self.size, DOUBLEBUF | HWSURFACE)

    def post_init(self):
        pygame.display.set_caption(TITLE)
        pygame.mixer.set_num_channels(SOUND_CHANNELS)
        pygame.key.set_repeat(500)
        self.fpsLimit = FPS_LIMIT
        self.fpsClock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 40)
        self.world = World()
        self.world.init()