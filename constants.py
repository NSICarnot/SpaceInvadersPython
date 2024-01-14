from game_states import GameState
# GAME VARIABLES

WIDTH: int = 900
HEIGHT: int = 700

BLACK: tuple[int, int, int] = (0, 0, 0)
WHITE: tuple[int, int, int] = (255, 255, 255)
GREEN: tuple[int, int, int] = (0, 255, 0)
PURPLE: tuple[int, int, int] = (100, 0, 255)

PLAYER_HEALTH: int = 3
PLAYER_SPEED: int = 1

SHIELD_HEIGHT: int = 450

GAME_STATE: GameState = GameState.PAUSE
