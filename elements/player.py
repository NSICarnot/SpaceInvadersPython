import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/player.png")
        self.rect = self.image.get_rect()
        self.__can_shoot: bool = True

    def get_rect(self) -> pygame.Rect:
        return self.rect

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y

    def move_right(self, x) -> None:
        self.rect.x += x

    def move_left(self, x) -> None:
        self.rect.x -= x

    def set_pos(self, x: int, y: int) -> None:
        self.rect.y = y
        self.rect.x = x

    def can_shoot(self, value: bool | None = None) -> bool | None:
        """
        The method will return a boolean if no value is passed in. Otherwise, the boolean value will be changed by the new value put in parameter.
        :param value: The value of the variable can_shoot
        """
        if not value:
            return self.__can_shoot
        else:
            self.__can_shoot = value
    
    def get_lifes_count() -> int:
        ...
        
    def set_lifes_count() -> None:
        ...
        
    def add_one_life() -> None:
        ...
        
    def remove_one_life() -> None:
        ...
