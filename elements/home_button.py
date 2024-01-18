import pygame
from game_states import GameState
import constants as c


class HomeButton:
    def __init__(self, x: int = 25, y: int = 25, width: int = 100, height = 50) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = c.GAME_FONT_20.render("Home", True, c.WHITE)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, c.PURPLE, (self.x, self.y, self.width, self.height), border_radius=15)
        screen.blit(self.text, (self.x + self.width / 2 - self.text.get_width() / 2, self.y + self.height / 2 - self.text.get_height() / 2))
        
    def set_game_scene(self) -> None:
        c.GAME_STATE = GameState.PLAY
        
    def get_rect(self) -> tuple[int, int, int, int]:
        return self.x, self.y, self.width, self.height
        