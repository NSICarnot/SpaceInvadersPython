import pygame
import constants as c


class Shield():
    def __init__(self, x: int, size: int) -> None:
        self.__pos: tuple[int] = (x, 750)  # The position anchor is the left bottom hand corner
        self.__size: int = size
        self.__pixels: list[Pixel] = []
        
    def get_pos(self) -> tuple[int]:
        return self.__pos
    
    def get_size(self) -> int:
        return self.__size
    
    def get_pixels(self) -> list[Pixel]:
        return self.__pixels
    
    def set_pos(self, x: int, y: int) -> None:
        ...
        

class Pixel():
    def __init__(self, x: int, y: int) -> None:
        self.__pos: tuple[int] = (x, y)
        
    def get_pos(self) -> tuple[int]:
        return self.__pos
    
    def set_pos(self, x: int, y: int) -> None:
        self.__pos = (x, y)
