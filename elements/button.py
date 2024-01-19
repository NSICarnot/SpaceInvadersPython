import pygame
from game_states import GameState
import constants as c


class Button:
    def __init__(self, x: int, y: int, width: int, height: int, text_color: tuple[int, int, int], text: str, background_color: tuple[int, int, int], border_radius: int = 15) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.text = c.GAME_FONT_20.render(text, True, c.WHITE)
        self.background_color = background_color
        self.border_radius = border_radius

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self.background_color, (self.x, self.y,
                         self.width, self.height), border_radius=self.border_radius)
        screen.blit(self.text, (self.x + self.width / 2 - self.text.get_width() /
                    2, self.y + self.height / 2 - self.text.get_height() / 2))

    def get_rect(self) -> tuple[int, int, int, int]:
        return self.x, self.y, self.width, self.height


class HomeButton(Button):
    def __init__(self, x: int = 25, y: int = 25, width: int = 100, height=50) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Home", c.PURPLE, 15)

    def set_game_scene(self) -> None:
        c.GAME_STATE = GameState.PLAY
        
class ApplyButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Apply", c.LIGHT_GREEN, 15)
        
    def apply_choice(self):
        ...
        
class RemoveButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Remove", c.LIGHT_GREEN, 15)
        
    def remove_choice(self):
        ...
