import pygame
from pygame.locals import *


def create_body(): # creates body block of snake
    surface.fill((255, 0, 255)) # to keep colour when body moving
    surface.blit(body, (body_x, body_y))
    pygame.display.flip()


if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 600))
    surface.fill((255, 0, 255))
    pygame.display.flip()

    body = pygame.image.load("resources/body.png").convert()
    body_x = 100
    body_y = 100
    surface.blit(body, (body_x, body_y))

    pygame.display.flip()

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == KEYDOWN: # key pressed
                if event.key == K_q:
                    playing = False
                if event.key == K_UP: # change pos y
                    body_y -= 10
                    create_body()
                if event.key == K_DOWN:
                    body_y += 10
                    create_body()
                if event.key == K_LEFT:
                    body_x -= 10
                    create_body()
                if event.key == K_RIGHT:
                    body_x += 10
                    create_body()
            elif event.type == QUIT:
                playing = False;
