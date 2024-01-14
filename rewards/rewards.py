import pygame

import constants as c


class Rewards:
    def __init__(self) -> None:
        self.items = {}
        self.font_size = 12
        self.image_size = 64

        # Container variables
        self.left_margin = 20
        self.top_margin = 225
        self.c_width = c.WIDTH - 2*self.left_margin
        self.c_height = c.HEIGHT - 2*self.top_margin
        
        # Scrollbar
        self.scrollbar = ScrollBar(2 * self.left_margin, c.HEIGHT - self.top_margin - 2 * self.left_margin, 100, self.left_margin, self.left_margin)

    def draw_container(self, screen: pygame.Surface) -> None:
        # TODO: Mettre bordures noires pour effet de disparition quand ça scrollera
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin),
                         (self.left_margin + self.c_width, self.top_margin), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin + self.c_height),
                         (self.left_margin + self.c_width, self.top_margin + self.c_height), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin),
                         (self.left_margin, self.top_margin + self.c_height), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin + self.c_width, self.top_margin),
                         (self.left_margin + self.c_width, self.top_margin + self.c_height), 3)
        
        self.scrollbar.draw(screen)
        
     
   
class ScrollBar(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, margin: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.margin: int = margin
        self.rect = pygame.Rect(x, y, width, height)
        
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, c.PURPLE, self.rect, border_radius=15)
        
    def set_pos(self, x: int, y: int) -> None:
        self.rect.x = x if 2 * self.margin <= x <= c.WIDTH - 2 * self.margin - self.width else self.rect.x
        self.rect.y = y
        
    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y
