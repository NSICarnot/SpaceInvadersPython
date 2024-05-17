import pygame
from pygame.sprite import Group
from elements.projectile import Projectile
import constants as c


class Invaders(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/ennemi1.png")
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y
        
    def shoot(self):
        ...

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def get_pos(self):
        return self.rect.x, self.rect.y
        