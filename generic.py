import pygame
from pygame.locals import *
from sys import exit

from game.object import Object

blueBox = Object()
redBox = Object()

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Generic")

running = True

clock = pygame.time.Clock()

blueBox.width, blueBox.height = 20, 20
blueBox.x, blueBox.y = 300, 300
blueBox.set_color((0, 0, 255))

redBox.width, redBox.height = 40, 40
redBox.x, redBox.y = 400, 400
redBox.set_color((255, 0, 0))


def control_movement(key_event, game_object):
    if event.type == KEYDOWN:
        if event.key == K_UP:
            game_object.mov_up()
            print(f"Moved Up: {game_object.y}")
        if event.key == K_DOWN:
            game_object.mov_down()
            print(f"Moved Down: {game_object.y}")
        if event.key == K_RIGHT:
            game_object.mov_right()
            print(f"Moved Right: {game_object.x}")
        if event.key == K_LEFT:
            game_object.mov_left()
            print(f"Moved Left: {game_object.x}")


def mouse_click_type(pressed):
    dict_mouse = {
        (1, 0, 0): "left",
        (0, 1, 0): "middle",
        (0, 0, 1): "right"
    }

    return dict_mouse.get(pressed)


while running:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        mouse = pygame.mouse

        if event.type == MOUSEBUTTONDOWN:
            mouse_x, mouse_y = mouse.get_pos()
            print(f'{mouse_x}, {mouse_y} | {mouse_click_type(mouse.get_pressed())}')

        control_movement(event, blueBox)

    screen.fill((0, 0, 0))
    blueBox.render(screen)
    redBox.render(screen)

    print(blueBox.rect)

    # if blueBox.is_collided_with(redBox):
    #     print('collision')

    pygame.display.update()
