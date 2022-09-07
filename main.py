import pygame
from pygame.locals import *


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.body = pygame.image.load("resources/body.png").convert()
        self.body_x = 100
        self.body_y = 100

    def draw(self): # creates body block of snake
        self.surface.fill((255, 0, 255)) # to keep colour when body moving
        self.screen.blit(self.body, (self.body_x, self.body_y))
        pygame.display.flip()

    def up_move(self):
        self.body_y -= 10
        self.draw()

    def down_move(self):
        self.body_y += 10
        self.draw()

    def left_move(self):
        self.body_x -= 10
        self.draw()

    def right_move(self):
        self.body_x += 10
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.surface.fill((255, 0, 255))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def play(self):
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == KEYDOWN:  # key pressed
                    if event.key == K_q:
                        playing = False
                    if event.key == K_UP:  # change pos y
                        self.snake.up_move()
                    if event.key == K_DOWN:
                        self.snake.down_move()
                    if event.key == K_LEFT:
                        self.snake.left_move()
                    if event.key == K_RIGHT:
                        self.snake.right_move()
                elif event.type == QUIT:
                    playing = False


if __name__ == "__main__":
    snake_game = Game()
    snake_game.run()
