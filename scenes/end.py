import pygame
import constants as c

from elements.button import HomePage, RestartButton, QuitButton

class End:
    def __init__(self):
        
        self.buttons_width = 250
        self.buttons_height = 75
        
        self.restart_button = RestartButton(25, 600, self.buttons_width, self.buttons_height)
        self.homepage_button = HomePage(325, 600, self.buttons_width, self.buttons_height)
        self.quit_button = QuitButton(625, 600, self.buttons_width, self.buttons_height)
        
    def draw(self, screen: pygame.Surface):
        """
        Dessine la scène à l'écran
        :param screen (pygame.Surface): L'écran
        :return (None): None
        """
        self.restart_button.draw(screen)
        self.homepage_button.draw(screen)
        self.quit_button.draw(screen)
        image_texte = c.GAME_FONT_100.render("GAME OVER", True, c.RED)
        screen.blit(image_texte, (175, 19))
        pygame.display.flip()
        