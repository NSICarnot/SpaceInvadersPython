import pygame
from pygame.sprite import Group
from elements.projectile import Projectile
import constants as c


class Invaders(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.x: float = x
        self.y: float = y
        self.images: list[pygame.Surface] = [pygame.transform.scale(pygame.image.load(f"img/ennemi1/ennemi{i}.png"), (45, 45)) for i in range(1, 5)]
        self.rect: pygame.Rect = self.images[0].get_rect()
        
        self.image_index: int = 0
        
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.image_index // 20], (self.x, self.y))
        
        self.image_index = self.image_index + 1 if not len(self.images) * 20 - 1 == self.image_index else 0

    def move(self, x, y) -> None:
        self.rect.x += x
        self.rect.y += y
        
    def shoot(self):
        ...

    def set_pos(self, x, y) -> None:
        self.rect.x = x
        self.rect.y = y

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y
        