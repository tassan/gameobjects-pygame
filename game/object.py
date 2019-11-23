"""
1. Colocar um objeto na tela
2. Mover um objeto

"""
import pygame


class Object:

    speed = 10
    length = 3

    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.color = (0, 0, 0)
        self.rect = None

    def set_color(self, rgb=(255, 255, 255)):
        self.color = rgb

    def on_pos(self, x, y):
        self.x = x
        self.y = y

    def render(self, screen):
        obj = pygame.Surface((self.width, self.height))
        obj.fill(self.color)
        self.rect = obj.get_rect()
        screen.blit(obj, (self.x, self.y))

    def is_collided_with(self, sprite):
        return self.rect.colliderect(sprite.rect)

    def mov_right(self):
        self.x += self.speed

    def mov_left(self):
        self.x = self.x - self.speed

    def mov_up(self):
        self.y = self.y - self.speed

    def mov_down(self):
        self.y = self.y + self.speed
