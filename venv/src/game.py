import pygame
from pygame.locals import *
import random
from block import B_block, T_block
from player import player

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

screen = pygame.display.set_mode([500, 700])
screen.fill(skyblue)

class game:
    def __init__(self):
        self.block_list = []
        self.score = 0
        self.G_over = 0
        self.x = 450
        self.h = random.choice(blist)
        self.th = self.h[1]
        self.bh = self.h[0]

    def gen_block(self):
        x = random.randint(480, 500)
        self.t_block = T_block(x, self.th, 'bpipe.png')
        self.b_block = B_block(x, self.bh, 'btpipe.png')
        self.t_blocks = pygame.sprite.Group()
        self.b_blocks = pygame.sprite.Group()
        self.t_blocks.add(self.t_block)
        self.b_blocks.add(self.b_block)
        self.all_sprites.add(self.b_blocks, self.t_blocks)

    def new_game(self):
        self.bird = player('flappy-bird.png', 150, 350, 2)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.bird)
        self.t_block = T_block(self.x, self.th, 'bpipe.png')
        self.b_block = B_block(self.x, self.bh, 'btpipe.png')
        self.t_blocks = pygame.sprite.Group()
        self.b_blocks = pygame.sprite.Group()
        self.t_blocks.add(self.t_block)
        self.b_blocks.add(self.b_block)
        self.all_sprites.add(self.b_blocks, self.t_blocks)
        self.G_over = 0
        self.score = 0

    def pause(self):
        cnt_pause = 1
        while cnt_pause == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        cnt_pause = 0
            self.display_text("pause", 250, 200, 32)
            pygame.display.flip()

    def gameover(self):
        self.G_over = 1
        while self.G_over == 1:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.G_over = 0
            self.display_text("GameOver!", 250, 200, 32)
            self.display_text("Press R to restart", 250, 300, 25)
            pygame.display.flip()
        self.new_game()

    def cnt_score(self):
        self.display_text("score : " +str(self.score), 50, 10, 20)

    def display(self):
        self.all_sprites.draw(screen)
        self.cnt_score()

    def event(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.pause()
            self.bird.Keypress(event)

    def update(self):
        self.all_sprites.update()
        Bbcollision = pygame.sprite.spritecollide(self.bird, self.b_blocks, True, pygame.sprite.collide_mask)
        Tbcollision = pygame.sprite.spritecollide(self.bird, self.t_blocks, True, pygame.sprite.collide_mask)
        if Bbcollision or Tbcollision:
            self.gameover()
        if self.t_block.rect.x < 150 and self.b_block.rect.x < 150:
            self.gen_block()
            self.score += 1
        if self.t_block.rect.x < 0:
            # self.
            pass


    def display_text(self, text, centerx, centery, size):
        font = pygame.font.Font('arial.ttf', size)
        render_text = font.render(text, True, black)
        text_rect = render_text.get_rect()
        text_rect.center = (centerx, centery)
        screen.blit(render_text, text_rect)

    def del_sprite(self):
        pass

    def run(self):
        while True:
            self.event()
            self.update()
            self.display()
            self.bird.player_gravity()
            pygame.display.flip()

g = game()
while g.run:
    g.new_game()
    g.run()