import pygame
from player import Player


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player: Player):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/projectile.png")
        self.rect = self.image.get_rect()
        self.__player = player

    def set_player_shoot_variable(self) -> None:
        self.__player.can_shoot(not self.__player.can_shoot())

    def set_pos(self, x: int, y: int):
        self.rect.y = y
        self.rect.x = x
    
    def draw(self, screen: pygame.Surface) -> None:
        ...