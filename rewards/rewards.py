import pygame

import constants as c


class Rewards:
    def __init__(self) -> None:
        self.items = {}
        self.font_size = 12
        self.image_size = 64
        
        # Container variables
        self.left_margin = 20
        self.top_margin = 250
        self.c_width = c.WIDTH - 2*self.left_margin
        self.c_height = c.HEIGHT - 2*self.top_margin
        
    def draw_container(self, screen: pygame.Surface):
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin), (self.left_margin + self.c_width, self.top_margin), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin + self.c_height), (self.left_margin + self.c_width, self.top_margin + self.c_height), 3)