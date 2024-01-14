import enum


class GameState(enum.Enum):
    PLAY: int = 0
    PAUSE: int = 1
    REWARDS: int = 2
    SCORE: int = 3
