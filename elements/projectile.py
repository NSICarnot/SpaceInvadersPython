import pygame


class Projectile(pygame.sprite.Sprite):
    def __init__(self, player: "Player"):  # type: ignore
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/projectile.png")
        self.rect = self.image.get_rect()
        self.__player = player
        
        self.rect.x = self.__player.get_pos()[0]
        self.rect.y = self.__player.get_pos()[1]

    def set_player_shoot_variable(self) -> None:
        self.__player.can_shoot(not self.__player.can_shoot())

    def set_pos(self, x: int, y: int):
        self.rect.y = y
        self.rect.x = x
    
    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, (self.rect.x - 7, self.rect.y))
        
    def get_x(self) -> int:
        return self.rect.x
    
    def get_y(self) -> int:
        return self.rect.y