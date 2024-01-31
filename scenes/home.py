import pygame
import constants as c

from elements.button import StartButton, RewardsButton, QuitButton  # TODO: Settings button

class Home:
    """
    Classe de la scène principale du jeu
    """
    def __init__(self) -> None:
        """
        Initialisation de la scène
        """
        self.buttons_width = 400
        self.buttons_height = 75
        
        self.start_button = StartButton(c.WIDTH / 2 - self.buttons_width / 2, 300, self.buttons_width, self.buttons_height)
        self.rewards_button = RewardsButton(c.WIDTH / 2 - self.buttons_width / 2, 400, self.buttons_width, self.buttons_height)
        self.quit_button = QuitButton(c.WIDTH / 2 - self.buttons_width / 2, 500, self.buttons_width, self.buttons_height)
    
    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine la scène à l'écrant
        :param screen (pygame.Surface): L'écrant
        :return (None): None
        """
        self.start_button.draw(screen)
        self.rewards_button.draw(screen)
        self.quit_button.draw(screen)
