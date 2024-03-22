import pygame
import constants as c
from game_states import GameState
from abc import abstractmethod


class Button:
    """
    Classe abstraite pour les boutons de l'application
    """
    def __init__(self, x: int, y: int, width: int, height: int, text_color: tuple[int, int, int], text: str, background_color: tuple[int, int, int], border_radius: int = 15) -> None:
        """
        Initialisation du bouton
        :param x (int): Coordonnée x du bouton
        :param y (int): Coordonnée y du bouton
        :param width (int): Largeur du bouton
        :param height (int): Hauteur du bouton
        :param text_color (tuple[int, int, int]): Couleur du texte
        :param background_color (tuple[int, int, int]): Couleur de l'arrière plan
        :param border_radius (int): Arrondissement des bordures
        :return (None): None
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_color = text_color
        self.text = c.GAME_FONT_20.render(text, True, c.WHITE)
        self.background_color = background_color
        self.border_radius = border_radius

    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine le bouton à l'écrant
        :param screen (pygame.Surface): L'écrant sur lequel dessiner
        :return (None): None
        """
        pygame.draw.rect(screen, self.background_color, (self.x, self.y,
                         self.width, self.height), border_radius=self.border_radius)
        screen.blit(self.text, (self.x + self.width / 2 - self.text.get_width() /
                    2, self.y + self.height / 2 - self.text.get_height() / 2))

    @abstractmethod
    def perform_action(self, *args) -> None:
        """
        Méthode abstraite pour le code à executer quand le bouton sera appuyé
        :param args (Any): Paramètres supplémentaires
        :return (None): None
        """
        pass

    def get_rect(self) -> tuple[int, int, int, int]:
        """
        Renvoie les coordonnées ainsi que la largeur et la hauteur du bouton
        :return (tuple[int, int, int, int]):
        """
        return self.x, self.y, self.width, self.height


class HomeButton(Button):
    def __init__(self, x: int = 25, y: int = 25, width: int = 100, height=50) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Home", c.PURPLE, 15)

    def perform_action(self) -> None:
        c.GAME_STATE = GameState.PLAY
        
class ApplyButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Apply", c.LIGHT_GREEN, 15)
        
    def perform_action(self):
        ...
        
class RemoveButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Remove", c.LIGHT_GREEN, 15)
        
    def perform_action(self):
        ...   

class ResumeButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Resume", c.LIGHT_GREEN, 15)
    
    def perform_action(self) -> None:
        c.GAME_STATE = GameState.PLAY
    
class RestartButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Restart", c.LIGHT_GREEN, 15)
        
    def perform_action(self) -> None:
        # TODO: Refresh all game variables
        c.GAME_STATE = GameState.PLAY
    
class QuitButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Quit", c.LIGHT_GREEN, 15)
        
    def perform_action(self) -> None:
        pygame.quit()
        exit()
        
class StartButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Start", c.LIGHT_GREEN, 15)
        
    def perform_action(self) -> None:
        c.GAME_STATE = GameState.PLAY
        
class RewardsButton(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Rewards", c.LIGHT_GREEN, 15)
        
    def perform_action(self) -> None:
        c.GAME_STATE = GameState.REWARDS
        
class HomePage(Button):
    def __init__(self, x: int, y: int, width: int, height: int, ) -> None:
        super().__init__(x, y, width, height, c.WHITE, "Homepage", c.LIGHT_GREEN, 15)
        
    def perform_action(self) -> None:
        c.GAME_STATE = GameState.SPLASH_SCREEN
