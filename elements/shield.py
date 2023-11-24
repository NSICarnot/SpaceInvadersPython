import pygame
import constants as c


class Pixel():
    def __init__(self, x: int, y: int, size: int) -> None:
        self.__size = size
        self.__rect = pygame.Rect(x, y, self.__size, self.__size)

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
            screen, c.GREEN, (self.__rect.x + 1, self.__rect.y + 1, self.__rect.x + self.__size - 1, self.__rect.y + self.__size - 1))


class Shield():
    def __init__(self, x: int, size: int) -> None:
        # The position anchor is the left top hand corner
        self.__pos: tuple[int] = (x, c.SHIELD_HEIGHT)
        self.__size: int = size
        self.__pixels: list[Pixel] = []

        # Create the shield Pixels list
        for y in range(10):
            self.__pixels.append([])
            for x in range(10):
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
                pixel.draw(screen)
