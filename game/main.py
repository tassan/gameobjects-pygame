import pygame
from pygame.locals import *
from sys import exit


class App:
    screenWidth = 800
    screenHeight = 600

    def __init__(self, running=True):
        self.RUNNING = running
        self.SCREEN = None
        self.COLOR = (0, 0, 0)

    def on_init(self, caption=None):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.screenWidth, self.screenHeight))

        pygame.display.set_caption(caption)

    def on_render(self):
        self.SCREEN.fill(self.COLOR)
        pygame.display.flip()

    def start(self):
        if not self.on_init():
            self.RUNNING = False

        while self.RUNNING:
            pygame.event.pump()
