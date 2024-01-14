import pygame
import constants as c
import time

from elements.player import Player
from elements.shield import Shield
from game_states import GameState
from rewards.rewards import Rewards

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

rewards_scene = Rewards()


def main() -> None:
    player_group.clear(surface=screen, bgd=pygame.Surface((c.WIDTH, c.HEIGHT)))
    player_group.draw(screen)

    shield.draw(screen)
    
    # Permet de faire bouger le vaisseau du joueur
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if player.rect.x < c.WIDTH - player.rect.width:
            player.move_right(c.PLAYER_SPEED)

    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if player.rect.x > 0:
            player.move_left(c.PLAYER_SPEED)


def rewards() -> None:
    rewards_scene.draw_container(screen)
    
    # Move scrollbar with keys
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        rewards_scene.scrollbar.set_pos(rewards_scene.scrollbar.rect.x - 1, rewards_scene.scrollbar.rect.y)
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        rewards_scene.scrollbar.set_pos(rewards_scene.scrollbar.rect.x + 1, rewards_scene.scrollbar.rect.y)
        
    # Move scrollbar with mouse
    """if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        x_offset = mouse_pos[0] - rewards_scene.scrollbar.rect.x
        if rewards_scene.scrollbar.rect.collidepoint((mouse_pos[0], mouse_pos[1])):
            rewards_scene.scrollbar.set_pos(pygame.mouse.get_pos()[0], rewards_scene.scrollbar.rect.y)"""

    
def pause() -> None:
    c.GAME_STATE = GameState.REWARDS
    

def score() -> None:
    ...


# Main loop of the game
while True:
    screen.fill(c.BLACK)

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
    
    match c.GAME_STATE:
        case GameState.PAUSE:
            pause()
        case GameState.PLAY:
            main()
        case GameState.REWARDS:
            rewards()
        case GameState.SCORE:
            score()

    clock.tick(240)

    # Update the screen
    pygame.display.update()
