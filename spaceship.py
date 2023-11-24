import pygame
import constants as t

class Spaceship:
    def __init__(self, x: int) -> None:
        self.__x: int = x
        self.__y: int = 750
        self.__can_shoot: bool = True
        
    def draw(screen: pygame.Surface) -> None:
        """
        Draw the ship
        :param screen(pygame.Surface):
        """
        pygame.draw.rect(screen, c.BLACK, (self.__x, self.__y, 30, 10))
        
    def get_pos() -> tuple[int, int]:
        """
        Return ship position
        :return (tuple[int, int]):
        """
        return self.__x, self.__y
    
    def can_shoot() -> bool:
        """
        Return True if the ship can shoot
        :return (bool):
        """
        return self.__can_shoot