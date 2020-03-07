import pygame
from pygame.locals import *
import sys
import random

pygame.init()

skyblue = (135, 206, 235)
white = (255, 255, 255)

WIN_WIDHT = 600
WIN_HEIGHT = 800

WINDOW = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGHT))
pygame.display.set_caption("flappy_bird")

WINDOW.fill(skyblue)

class Player:

    def __init__(self, x, y, image):
        self.img = pygame.transform.scale(pygame.image.load(image), (50, 50))
        self.x = x
        self.y = y
        self.vel = 0
        self.height = self.y
        self.gravity = 9.8

    def jump(self):
        self.y = -10
        self.height = self.y

    def move(self):
        self.y -= self.gravity

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)



class Pipe:
    def __init__(self, x):
        self.vel = 5
        self.top_image = pygame.image.load("img\\pipe_top.png")
        self.bottom_image = pygame.image.load("img\\pipe_bottom.png")
        self.x = x
        self.win_height = WIN_HEIGHT
        self.win_width = WIN_WIDHT
        self.set_y()


    def set_y(self):
        self.y = random.randrange(50, 310)
        self.top = self.y - self.top_image.get_height()
        self.bottom = self.y + 200 #gap at top between bottom

    def move(self):
        self.x -= self.vel

    def display(self, window):
        window.blit(self.top_image, (self.x, self.top))
        window.blit(self.bottom_image, (self.x, self.bottom))

    def collide(self, bird, win):
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.top_image)
        bottom_mask = pygame.mask.from_surface(self.bottom_image)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if b_point and t_point:
            return True

        return False


def draw_text(text):
    return pygame.font.Font.render('arial', "Score: " + str(text), 1, (255, 255, 255))

def game_window(win, bird, pipes, score):

    for pipe in pipes:
        pipe.display(win)

    bird.draw(win)

    pygame.display.update()

def main():
    score = 0
    bird = Player(230, 350, 'img\\flappy-bird.png')
    pipe = [Pipe(700)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_start = True
                    bird.jump()

        game_window(WINDOW, bird, pipe, score)







if __name__ == "__main__":
    main()