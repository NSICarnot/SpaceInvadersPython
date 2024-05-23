from game_states import GameState
from pygame import font
# GAME VARIABLES

WIDTH: int = 900
HEIGHT: int = 700

BLACK: tuple[int, int, int] = (0, 0, 0)
WHITE: tuple[int, int, int] = (255, 255, 255)
LIME: tuple[int, int, int] = (0, 255, 0)
LIGHT_GREEN: tuple[int, int, int] = (0, 190, 0)
DARK_GREEN: tuple[int, int, int] = (0, 100, 0)
PURPLE: tuple[int, int, int] = (100, 0, 255)
RED: tuple[int, int, int] = (255, 0, 0)

PLAYER_HEALTH: int = 3
PLAYER_SPEED: int = 2

PROJECTILE_SPEED: int = 3

SHIELD_HEIGHT: int = 450

GAME_STATE: GameState = GameState.SPLASH_SCREEN

GAME_FONT_20: font.Font = font.Font("./font/font.ttf", 20)
GAME_FONT_100: font.Font = font.Font("./font/font.ttf", 100)

