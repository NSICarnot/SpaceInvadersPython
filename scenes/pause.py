import pygame
import constants as c

from elements.button import HomePage, ResumeButton, RestartButton, QuitButton

class Pause:
    def __init__(self) -> None:
        self.buttons_width = 400
        self.buttons_height = 75
        
        self.homepage_button = HomePage(c.WIDTH / 2 - self.buttons_width / 2, 200, self.buttons_width, self.buttons_height)
        self.resume_button = ResumeButton(c.WIDTH / 2 - self.buttons_width / 2, 300, self.buttons_width, self.buttons_height)
        self.restart_button = RestartButton(c.WIDTH / 2 - self.buttons_width / 2, 400, self.buttons_width, self.buttons_height)
        self.quit_button = QuitButton(c.WIDTH / 2 - self.buttons_width / 2, 500, self.buttons_width, self.buttons_height)
    
    def draw(self, screen: pygame.Surface) -> None:
        self.homepage_button.draw(screen)
        self.resume_button.draw(screen)
        self.restart_button.draw(screen)
        self.quit_button.draw(screen)