import pygame

import constants as c


class Rewards:
    def __init__(self) -> None:
        self.font_size = 12
        self.image_size = 64

        # Container variables
        self.left_margin = 20
        self.top_margin = 225
        self.c_width = c.WIDTH - 2*self.left_margin
        self.c_height = c.HEIGHT - 2*self.top_margin
        
        self.items = [
            _Item(100, self.top_margin + 2 * self.left_margin, "img\projectile.png", "Test", 0),
            _Item(200, self.top_margin + 2 * self.left_margin, "img\projectile.png", "Test2", 0),
            _Item(300, self.top_margin + 2 * self.left_margin, "img\projectile.png", "Test3", 0)
        ]

        # Scrollbar
        self.scrollbar = _ScrollBar(2 * self.left_margin, c.HEIGHT - self.top_margin -
                                    2 * self.left_margin, 100, self.left_margin, self.left_margin)

    def draw_container(self, screen: pygame.Surface) -> None:
        # TODO: Draw items first
        for item in self.items:
            item.draw(screen)

        # Black effect
        pygame.draw.rect(screen, c.BLACK, (0, self.top_margin + self.left_margin,
                         4 * self.left_margin - 1, self.top_margin - 2 * self.left_margin))
        pygame.draw.rect(screen, c.BLACK, (c.WIDTH - 4 * self.left_margin - 1, self.top_margin +
                         self.left_margin, 4 * self.left_margin, self.top_margin - 2 * self.left_margin))

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


class _ScrollBar(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, margin: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.width = width
        self.margin: int = margin
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, c.PURPLE, self.rect, border_radius=15)

    def set_pos(self, x: int, y: int) -> None:
        self.rect.x = x if 2 * self.margin <= x <= c.WIDTH \
            - 2 * self.margin - self.width else self.rect.x
        self.rect.y = y

    def get_pos(self) -> tuple[int, int]:
        return self.rect.x, self.rect.y


class _Item:
    def __init__(self, x: int, y: int, image_path, name: str, rarity: int) -> None:
        self.x = x
        self.y = y
        self.item_image: pygame.Surface = pygame.transform.scale(pygame.image.load(image_path), (64, 64))
        self.name = name
        self.rarity = rarity

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.line(screen, c.PURPLE, (self.x, self.y),
                         (self.x + 96, self.y))
        pygame.draw.line(screen, c.PURPLE,
                         (self.x, self.y + 128), (self.x + 96, self.y + 128))
        pygame.draw.line(screen, c.PURPLE, (self.x, self.y),
                         (self.x, self.y + 128))
        pygame.draw.line(screen, c.PURPLE, (self.x + 96,
                         self.y), (self.x + 96, self.y + 128))

        screen.blit(self.item_image, (self.x + 16, self.y + 16))
        text = c.GAME_FONT.render(self.name, True, c.WHITE)
        screen.blit(text, (self.x + (48 - text.get_width() / 2), self.y + 100))
