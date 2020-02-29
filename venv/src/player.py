import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, image, posx, posy, speed):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.posx = posx
        self.posy = posy
        self.vy = 0
        self.gravity = 0.005
        self.speed = speed
        self.Jump = 0
        self.mask_size = self.p_mask.get_size()
        self.mask_size = (100, 100)

    def Keypress(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.Jump = 1

    def jump(self):
        if self.rect.top > 0:
            self.vy -= self.Jump
        self.Jump = 0
        if self.rect.top < 0:
            self.vy = 0.25
            self.p_mask = pygame.mask.from_surface(self.image)

    def move(self):
        y = self.posy
        self.posy = y + self.vy

    def player_gravity(self):
        self.vy += self.gravity

    # def display(self, screen):
    #     self.rect.center = (self.posx, self.posy)
    #     self.p_mask = pygame.mask.from_surface(self.image)

class player(pygame.sprite.Sprite):
    def __init__(self, image, posx, posy):
        super.__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = (posx, posy)

    def update(self, *args):

