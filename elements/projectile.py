import pygame
from player import Player


class Projectile(pygame.sprite.Sprite):
    def __init__(self, master: Player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/projectile.png")
        self.rect = self.image.get_rect()
        self.__master = master

    def set_master_shoot_variable(self) -> None:
        self.__master.can_shoot(not self.__master.can_shoot())

    def set_pos(self, x: int, y: int):
        self.rect.y = y
        self.rect.x = x
