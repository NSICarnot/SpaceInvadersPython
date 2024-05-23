import pygame
import json

import constants as c
from elements.button import HomeButton, ApplyButton, RemoveButton


class Rewards:
    """
    Classe de la scène des récompences
    """
    def __init__(self) -> None:
        """
        Inistialisation de la scène
        """
        self.image_size = 64
        self.spacement = 120
        self.json_reward = ...

        # Container variables
        self.left_margin = 20
        self.top_margin = 225
        self.c_width = c.WIDTH - 2 * self.left_margin
        self.c_height = c.HEIGHT - 2 * self.top_margin
        
        self.items = [
            _Item(self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test", 0),
            _Item(2 * self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test2", 0),
            _Item(3 * self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test3", 0),
            _Item(4 * self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test4", 0),
            _Item(5 * self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test5", 0),
            _Item(6 * self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test6", 0),
            _Item(7 * self.spacement, self.top_margin + 2 * self.left_margin, "./img/projectile/projectile1.png", "Test7", 0),
        ]

        # Scrollbar
        self.scrollbar = _ScrollBar(2 * self.left_margin, c.HEIGHT - self.top_margin -
                                    2 * self.left_margin, 100, self.left_margin, self.left_margin)
        self.home_button = HomeButton()
        self.apply_button = ApplyButton(166, 550, 200, 75)  # TODO: Fix the button position
        self.remove_button = RemoveButton(532, 550, 200, 75)  # TODO: Fix the button position

    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine la scène à l'écrant
        :param screen (pygame.Surface): L'écran
        """
        # TODO: Draw items first
        for i, item in enumerate(self.items):
            item.set_pos((i + 1) * self.spacement - self.scrollbar.get_percent() * (c.WIDTH / self.spacement), item.get_pos()[1])
            item.draw(screen)

        # Black effect
        pygame.draw.rect(screen, c.BLACK, (0, self.top_margin + self.left_margin,
                         4 * self.left_margin - 1, self.top_margin - 2 * self.left_margin))
        pygame.draw.rect(screen, c.BLACK, (c.WIDTH - 4 * self.left_margin, self.top_margin +
                         self.left_margin, 4 * self.left_margin, self.top_margin * self.left_margin))

        # Container borders
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin),
                         (self.left_margin + self.c_width, self.top_margin), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin + self.c_height),
                         (self.left_margin + self.c_width, self.top_margin + self.c_height), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin, self.top_margin),
                         (self.left_margin, self.top_margin + self.c_height), 3)
        pygame.draw.line(screen, c.PURPLE, (self.left_margin + self.c_width, self.top_margin),
                         (self.left_margin + self.c_width, self.top_margin + self.c_height), 3)

        self.scrollbar.draw(screen)
        self.home_button.draw(screen)
        self.apply_button.draw(screen)
        self.remove_button.draw(screen)
        
    def get_home_button(self) -> HomeButton:
        """
        Renvoie le bouton pour aller à l'accueil
        :return (Button):
        """
        return self.home_button


class _ScrollBar(pygame.sprite.Sprite):
    """
    Classe permettant de gérer la scrollbar
    """
    def __init__(self, x: int, y: int, width: int, height: int, margin: int) -> None:
        """
        Initialisation de la scrollbar
        :param x (int): Position x de la scrollbar
        :param y (int): Position y de la scrollbar
        :param width (int): Largeur de la scrollbar
        :param height (int): Hauteur de la scrollbar
        :param margin (int): Marge de la scrollbar
        :return (None): None
        """
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.width = width
        self.margin: int = margin
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine la scrollbar à l'écrant
        :param screen (pygame.Surface): L'écrant
        :return (None): None
        """
        pygame.draw.rect(screen, c.PURPLE, self.rect, border_radius=15)

    def set_pos(self, x: int, y: int) -> None:
        """
        Défini la position de la scrollbar
        :param x (int): Coordonnée x du bouclier
        :param y (int): Coordonnée y du bouclier
        :return (None): None
        """
        self.rect.x = x if 2 * self.margin <= x <= c.WIDTH \
            - 2 * self.margin - self.width else self.rect.x
        self.rect.y = y

    def get_pos(self) -> tuple[int, int]:
        """
        Renvoie la position de la scrollbar
        :return (tuple[int, int]):
        """
        return self.rect.x, self.rect.y
    
    def get_percent(self) -> float:
        """
        Renvoie le pourcentage progression de la scrollbar
        :return (int):
        """
        stop = c.WIDTH - 2 * self.margin - self.width
        return ((self.rect.x - self.x) * 100) / (stop - self.x)
    
    def get_width(self) -> int:
        """
        Renvoie la largeur de la scrollbar
        :return (int):
        """
        return self.width


class _Item:
    """
    Classe des éléments de récompenses
    """
    def __init__(self, x: int, y: int, image_path, name: str, rarity: int) -> None:
        """
        Initialisation des éléments 
        :param x (int): Coordonnée x de l'élément 
        :param y (int): Coordonnée y de l'élément
        :param image_path (str): Chemin de l'image de l'élément
        :param rarity (int): Rereté de l'élément
        :return (None): None
        """
        self.x = x
        self.y = y
        self.item_image: pygame.Surface = pygame.transform.scale(pygame.image.load(image_path), (64, 64))
        self.name = name
        self.rarity = rarity

    def draw(self, screen: pygame.Surface) -> None:
        """
        Dessine l'élément à l'écrant
        :param screen (pygame.Surface): L'écrant
        :return (None): None
        """
        pygame.draw.line(screen, c.PURPLE, (self.x, self.y),
                         (self.x + 96, self.y))
        pygame.draw.line(screen, c.PURPLE,
                         (self.x, self.y + 128), (self.x + 96, self.y + 128))
        pygame.draw.line(screen, c.PURPLE, (self.x, self.y),
                         (self.x, self.y + 128))
        pygame.draw.line(screen, c.PURPLE, (self.x + 96,
                         self.y), (self.x + 96, self.y + 128))

        screen.blit(self.item_image, (self.x + 16, self.y + 16))
        text = c.GAME_FONT_20.render(self.name, True, c.WHITE)
        screen.blit(text, (self.x + (48 - text.get_width() / 2), self.y + 100))
        
    def get_pos(self) -> tuple[int, int]:
        """
        Renvoie la position de l'élément
        :return (tuple[int, int]):
        """
        return self.x, self.y
    
    def set_pos(self, x: int, y: int) -> None:
        """
        Défini la position de l'élément'
        :param x (int): Coordonnée x de l'élément
        :param y (int): Coordonnée y de l'élément
        :return (None): None
        """
        self.x = x
        self.y = y
