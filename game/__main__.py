import pygame
from pygame.locals import *
from sys import exit


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

    @staticmethod
    def on_event():
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

    def start(self, game_name):
        self.on_init(game_name)

        while self.RUNNING:
            self.on_render()
            self.on_event()


if __name__ == "__main__":
    game = App()
    game.start("Game Name")
