import enum


class GameState(enum.Enum):
    """
    Classe d'énumération des différents états du jeu
    """
    PLAY: int = 0
    PAUSE: int = 1
    REWARDS: int = 2
    SCORE: int = 3
    SPLASH_SCREEN: int = 4
    SETTINGS: int = 5
