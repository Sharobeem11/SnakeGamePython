import pygame
from pygame.locals import *
import time
import random

SIZE = 30  # constant of size of one body part


class Food:
    def __init__(self, screen):
        self.food = pygame.image.load("resources/apple.png").convert()
        self.screen = screen
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.screen.blit(self.food, (self.x, self.y))
        pygame.display.flip()

    def pos_change(self):
        self.x = random.randint(0, 29)*SIZE
        self.y = random.randint(0, 19)*SIZE


class Snake:
    def __init__(self, screen, length):
        self.length = length
        self.screen = screen
        self.body = pygame.image.load("resources/body.png").convert()
        self.body_x = [SIZE] * length  # how many body parts
        self.body_y = [SIZE] * length
        self.dir = "up"

    def add_length(self):
        self.length += 1
        self.body_x.append(-1)
        self.body_y.append(-1)

    def draw(self): # creates body block of snake
        self.screen.fill((255, 0, 255))  # to keep colour when body moving
        for item in range(self.length):
            self.screen.blit(self.body, (self.body_x[item], self.body_y[item]))
        pygame.display.flip()

    def move(self): # move body parts to take pos of previous
        for item in range(self.length-1, 0, -1):
            self.body_x[item] = self.body_x[item - 1]
            self.body_y[item] = self.body_y[item - 1]

        if self.dir == "up":
            self.body_y[0] -= SIZE
        if self.dir == "down":
            self.body_y[0] += SIZE
        if self.dir == "left":
            self.body_x[0] -= SIZE
        if self.dir == "right":
            self.body_x[0] += SIZE
        self.draw()

    def up_move(self):
        self.dir = "up"

    def down_move(self):
        self.dir = "down"

    def left_move(self):
        self.dir = "left"

    def right_move(self):
        self.dir = "right"


class Game:
    def __init__(self):
        pygame.init()
        self.surface = pygame.display.set_mode((900, 600))
        self.surface.fill((255, 0, 255))
        self.snake = Snake(self.surface, 1)
        self.snake.draw()
        self.food = Food(self.surface)
        self.food.draw()

    def is_hit(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False

    def score(self):
        font = pygame.font.SysFont("arial", 30)
        score = font.render(f"Score: {self.snake.length}", True, (255, 255, 255))
        self.surface.blit(score, (0, 0))

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

            self.snake.move()
            self.food.draw()
            self.score()
            pygame.display.flip()

            if self.is_hit(self.snake.body_x[0], self.snake.body_y[0], self.food.x, self.food.y):
                self.snake.add_length()
                self.food.pos_change()
            time.sleep(0.3)


if __name__ == "__main__":
    snake_game = Game()
    snake_game.play()
