import pygame

pygame.init()

class B_block(pygame.sprite.Sprite):
    def __init__(self, x, h, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (80, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0

    def update(self):
        self.rect.x -= 1
        self.block_mask = pygame.mask.from_surface(self.image)

class T_block(pygame.sprite.Sprite):
    def __init__(self, x, h, image):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (80, h))
        self.rect.x = x
        self.rect.y = 700 - h

    def update(self):
        self.rect.x -= 1
        self.block_mask = pygame.mask.from_surface(self.image)