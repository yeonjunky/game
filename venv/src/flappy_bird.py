import pygame
from pygame.locals import *
import random

pygame.init()

blist=[[50,310],[60,300],[70,290],[80,280],[90,270],[100,260],[110,250],[120,240],[130,230],[140,220],[150,210],[160,200],[170,190],[180,180],
       [190,170],[200,160],[210,150],[220,140],[230,130],[240,120],[250,110],[260,100],[270,90],[280,80]
       ,[290,70],[300,60],[310,50]]
black = (255,255,255)
white = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
skyblue = (135, 206, 235)

WIN_WIDHT = 600
WIN_HEIGHT = 800

WINDOW = pygame.display.set_mode((WIN_WIDHT, WIN_HEIGHT))
pygame.display.set_caption("flappy_bird")

WINDOW.fill(skyblue)

class player:

    def __init__(self, x, y, image):
        self.img = pygame.image.load(image)
        self.x = x
        self.y = y
        self.vel = 0
        self.height = self.y

    def jump(self):
        self.vel = -10
        self.height -= self.y

    def move(self):
        pass

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))


    def get_mask(self):
        return pygame.mask.from_surface(self.img)



class pipe:
    def __init__(self, x):
        self.vel = 5
        self.top_image = pygame.image.load("img/pipe_top.png")
        self.bottom_image = pygame.image.load("img/pipe_bottom.png")
        self.x = x

    def set_y(self):
        y = random.choice(blist)
        self.top = y[0]
        self.bottom = y[1]

    def move(self):
        self.x -= self.vel

    def display(self, win):
        win.bilt(self.top_image, (self.x, self.top))
        win.bilt(self.bottom_image, (self.x, self.bottom))

    def collide(self):
        pygame.sprite.collide_mask()

def main():
    score = 0
    bird = player(230, 350)

if __name__ == "__main__":
    main()