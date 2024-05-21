class Score:
    """Classe de la scène de score après la mort du joueur"""
    def __init__(self) -> None:
        self.__score: int = 0
        self.__multiplier: float = 1.1

    def score(self) -> None:
        self.__score *= self.__multiplier

    def get_score(self) -> float:
        return self.__score