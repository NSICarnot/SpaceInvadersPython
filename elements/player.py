import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/player.png")
        self.rect = self.image.get_rect()
        self.__can_shoot: bool = True
        self.lifes: int = 3
        self.died: bool = False

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
    
    def get_lifes_count(self) -> int:
        """
        Return the number of lifes of the player
        :return: The number of lifes of the player
        """
        return self.lifes
        
    def set_lifes_count(self, new: int) -> None:
        """
        Set the number of lifes of the player
        :param new: The new number of lifes of the player
        :return: None
        """
        assert new > 3, "Le joueur ne peut avoir que trois vie max"
        if new == 0:
            self.died = True
        self.lifes = new
        
    def add_one_life(self) -> None:
        """
        Add one life to the player
        :return: None
        """
        assert 1 + self.lifes > 3, "Le joueur ne peut avoir que trois vie max"
        self.lifes += 1
        if self.lifes == 0:
            self.died = True
        else:
            self.died = False
        
    def remove_one_life(self) -> None:
        """
        Remove one life to the player
        :return: None
        """
        assert self.lifes == 0, "Le nombre de vie du joueur est déjà au minimum."
        self.lifes -= 1
        if self.lifes == 0:
            self.died = True
        else:
            self.died = False

    def is_died(self) -> bool:
        """
        Return a boolean if the player is died or not
        :return: A boolean if the player is died or not
        """
        return self.died