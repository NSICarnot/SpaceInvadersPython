import pygame
from helper import load_image


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player: "Player"):  # type: ignore
        pygame.sprite.Sprite.__init__(self)
        self.images: list[pygame.Surface] = [load_image(f"img/projectile/projectile{i}.png") for i in (1, 2)]
        self.rect: pygame.Rect = self.images[0].get_rect()
        self.__player = player
        
        self.rect.x = self.__player.get_pos()[0] + self.__player.get_rect().width / 2 - self.rect.width / 2
        self.rect.y = self.__player.get_pos()[1]
        
        self.image_index: int = 0

    def set_player_shoot_variable(self) -> None:
        self.__player.can_shoot(not self.__player.can_shoot())

    def set_pos(self, x: int, y: int) -> None:
        self.rect.y = y
        self.rect.x = x
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.images[self.image_index // 20], (self.rect.x, self.rect.y))
        self.image_index = self.image_index + 1 if not len(self.images) * 20 - 1 == self.image_index else 0
        
    def get_x(self) -> int:
        return self.rect.x
    
    def get_y(self) -> int:
        return self.rect.y