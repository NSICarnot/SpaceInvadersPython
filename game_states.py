import enum


class GameState(enum.Enum):
    PLAY: int = 0
    PAUSE: int = 1
    REWARDS: int = 2
    SCORE: int = 3
    SPLASH_SCREEN: int = 4
    SETTINGS: int = 5
