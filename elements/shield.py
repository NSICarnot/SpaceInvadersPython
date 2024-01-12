import pygame
import math
import random as r

import constants as c


class Pixel():
    def __init__(self, x: int, y: int, size: int) -> None:
        self.__size: int = size
        self.__rect: pygame.Rect = pygame.Rect(x, y, self.__size, self.__size)

    def get_pos(self) -> tuple[int]:
        return self.__pos

    def get_size(self) -> int:
        return self.__size

    def set_pos(self, x: int, y: int) -> None:
        self.__pos = (x, y)

    def set_size(self, size: int) -> None:
        self.__size = size

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen, c.GREEN, (self.__rect.x, self.__rect.y, self.__size, self.__size))


class Shield():
    def __init__(self, x: int, size: int) -> None:
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
        return self.__pos

    def get_size(self) -> int:
        return self.__size

    def get_pixels(self) -> list[Pixel]:
        return self.__pixels

    def set_pos(self, x: int, y: int) -> None:
        self.__pos = (x, y)

    def set_pixels(self, pixels: list[Pixel]) -> None:
        self.__pixels = pixels

    def draw(self, screen: pygame.Surface) -> None:
        for p_line in self.__pixels:
            for pixel in p_line:
                if pixel != None:
                    pixel.draw(screen)

    def blow_up_pixels(self, x: int, y: int, radius: float) -> None:
        """
        Pop the calculated pixels which were in the radius of the explosion
        :param x: The x coordinate of the impact
        :param y: The y coordinate of the impact 
        """
        for yp, p_line in enumerate(self.__pixels):
            for xp, _ in enumerate(p_line):
                rand: int = r.randint(1, 5)
                if not rand == 3:
                    if math.sqrt((xp - x) ** 2 + (yp - y) ** 2) <= radius:
                        self.__pixels[yp].pop(xp)
                        self.__pixels[yp].insert(xp, None)
