import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/player.png")
        self.rect = self.image.get_rect()

    def set_pos(self, x: int, y: int):
        self.rect.y = y
        self.rect.x = x
    