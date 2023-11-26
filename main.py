import pygame
import constants as c
import time

from elements.player import Player
from elements.shield import Shield

# Initialize the pygame window
pygame.init()

# Create the screen and setting up its name
screen: pygame.Surface = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("SpaceInvaders - NSI 1ere 2023-2024")


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
player.set_pos(c.WIDTH//2, 550)

shield = Shield(100, 1)

# Main loop of the game
while True:
    screen.fill(c.BLACK)

    player_group.clear(surface=screen, bgd=pygame.Surface((c.WIDTH, c.HEIGHT)))
    player_group.draw(screen)

    shield.draw(screen)

    # Parsing all pygame events
    for event in pygame.event.get():
        # Chacking the events type
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill(c.BLACK)
            if event.key == pygame.K_a:
                shield.blow_up_pixels(50, 0, 15)

    # Permet de faire bouger le vaisseau du joueur
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if player.rect.x < c.WIDTH - player.rect.width:
            player.move_right(c.PLAYER_SPEED)

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if player.rect.x > 0:
            player.move_left(c.PLAYER_SPEED)

    clock.tick(240)

    # Update the screen
    pygame.display.update()
