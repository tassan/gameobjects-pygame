import pygame
from pygame.locals import *
from sys import exit

from game import object

obj = object.Object()


class App:
    screenWidth = 800
    screenHeight = 600

    def __init__(self):
        self.RUNNING = True
        self.screen = None

    def on_init(self, caption=""):
        pygame.init()
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.screen.fill((0, 0, 0))
        pygame.display.set_caption(caption)

    @staticmethod
    def on_render():
        pygame.display.update()

    def start(self, game_name):
        self.on_init(game_name)
        self.on_render()
        while self.RUNNING:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

            obj.on_pos(300, 300)
            obj.render()

            pygame.display.update()


if __name__ == "__main__":
    game = App()
    game.start("Game Name")
