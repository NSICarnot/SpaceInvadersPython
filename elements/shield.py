import pygame
import math
import random as r

import constants as c


class Pixel():
    """
    Classe des pixels composants le bouclier
    """
    def __init__(self, x: int, y: int, size: int) -> None:
        """
        Initialisation du pixel
        :param x (int): Coordonnée x du pixel
        :param y (int): Coordonnée y du pixel
        :param size (int): Taille du bouclier en pixel
        """
        self.__size: int = size
        self.__rect: pygame.Rect = pygame.Rect(x, y, self.__size, self.__size)

    def get_pos(self) -> tuple[int]:
        """
        Renvoie la position du pixel
        :return (tuple[int, int]):
        """
        return self.__pos

    def get_size(self) -> int:
        """
        Renvoie la taille des pixels
        :return (int):
        """
        return self.__size

    def set_pos(self, x: int, y: int) -> None:
        """
        Défini la position du pixel
        :param x (int): Coordonnée x du pixel
        :param y (int): Coordonnée y du pixel
        :return (None): None
        """
        self.__rect.x = x
        self.__rect.y = y

    def set_size(self, size: int) -> None:
        """
        Défini la taille des pixels
        :param size (int): Taille en pixel
        :return (None): None
        """
        self.__size = size

    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine à l'écrant le pixel
        :param screen (pygame.Surface): L'écrant
        :return (None):
        """
        pygame.draw.rect(
            screen, c.LIME, (self.__rect.x, self.__rect.y, self.__size, self.__size))


class Shield():
    def __init__(self, x: int, size: int) -> None:
        """
        Initialisation du bouclier
        :param x (int): Coordonnée x du bouclier
        :param y (int): Coordonnée y du bouclier
        :param size (int): Nombre de pixels (Pixel) dans le bouclier
        :return (None):
        """
        # The position anchor is the left top hand corner
        self.__pos: tuple[int] = (x, c.SHIELD_HEIGHT)
        self.__size: int = size
        self.__pixels: list[list[Pixel | None]] = []

        # Create the shield Pixels list
        for y in range(100):
            self.__pixels.append([])
            for x in range(100):
                self.__pixels[y].append(
                    Pixel(self.__pos[0] + x * self.__size, self.__pos[1] + y * self.__size, self.__size))

    def get_pos(self) -> tuple[int]:
        """
        Renvoie la position du bouclier
        :return (tuple[int, int]):
        """
        return self.__pos

    def get_size(self) -> int:
        """
        Renvoie la taille du bouclier
        :return (int):
        """
        return self.__size

    def get_pixels(self) -> list[list[Pixel | None]]:
        """
        Renvoie la liste contenant les pixels
        :return (list[list[Pixel | None]]):
        """
        return self.__pixels

    def set_pos(self, x: int, y: int) -> None:
        """
        Défini la position du pixel
        :param x (int): Coordonnée x du bouclier
        :param y (int): Coordonnée y du bouclier
        :return (None): None
        """
        self.__pos = (x, y)

    def set_pixels(self, pixels: list[list[Pixel | None]]) -> None:
        """
        Défini la liste contenant les pixels
        :param pixels (list[list[Pixel | None]]): Liste de liste de Pixel
        :return (None): None
        """
        self.__pixels = pixels

    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine le bouclier
        :param screen (pygame.surface): L'écrant"""
        for p_line in self.__pixels:
            for pixel in p_line:
                if pixel != None:
                    pixel.draw(screen)

    def blow_up_pixels(self, x: int, y: int, radius: float) -> None:
        """
        Pop with a chance of 20% the calculated pixels which were in the radius of the explosion . Somme pixels won't be deleted to looks like the original game.
        :param x (int): The x coordinate of the impact
        :param y (int): The y coordinate of the impact 
        """
        for yp, p_line in enumerate(self.__pixels):
            for xp, _ in enumerate(p_line):
                rand: int = r.randint(1, 5)
                if not rand == 3:
                    if math.sqrt((xp - x) ** 2 + (yp - y) ** 2) <= radius:
                        self.__pixels[yp].pop(xp)
                        self.__pixels[yp].insert(xp, None)
