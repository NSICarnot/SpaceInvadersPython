import pygame
import constants as c
import random
from elements.player import Player
import time

# Initialize the pygame window
pygame.init()

# Create the screen and setting up its name
screen = pygame.display.set_mode((c.WIDTH, c.HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("SpaceInvaders - NSI 1ere 2023-2024")


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)
player.set_pos(x=c.WIDTH//2, y=550)

# Main loop of the game
while True:
    player_group.clear(surface=screen, bgd=pygame.Surface((c.WIDTH, c.HEIGHT)))
    player_group.draw(screen)
    
    # Parsing all pygame events
    for event in pygame.event.get():
        # Chacking the events type
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((0, 0, 0))
    
    # Permet de faire bouger le vaisseau du joueur
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if player.rect.x < c.WIDTH - player.rect.width:
            player.set_pos(x=player.rect.x + 1, y=550)
    
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if player.rect.x > 0:
            player.set_pos(x=player.rect.x - 1, y=550)

    time.sleep(0.005)

    clock.tick(240)
    
    # Update the screen
    pygame.display.flip()