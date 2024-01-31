import pygame

# Initialize the pygame window
pygame.init()
pygame.font.init()

import constants as c
import backend.helper as helper

from elements.player import Player
from elements.shield import Shield
from game_states import GameState
from scenes.home import Home
from scenes.pause import Pause
from scenes.rewards.rewards import Rewards


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
splash_screen_scene = Home()
pause_scene = Pause()


def main() -> None:
    """
    Boucle principale du jeu 
    """
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
            
    if pygame.key.get_pressed()[pygame.K_ESCAPE]:
        c.GAME_STATE = GameState.PAUSE


def rewards() -> None:
    """
    Affiche la scène des récompenses
    """
    rewards_scene.draw(screen)
    
    # Move scrollbar with keys
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        rewards_scene.scrollbar.set_pos(rewards_scene.scrollbar.rect.x - 1, rewards_scene.scrollbar.rect.y)
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        rewards_scene.scrollbar.set_pos(rewards_scene.scrollbar.rect.x + 1, rewards_scene.scrollbar.rect.y)
    
    # TODO: Si plus sur la scrollbar mais tjr appuyé: alors continuer de bouger la scrollbar
    # Move scrollbar with mouse
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        if rewards_scene.scrollbar.rect.collidepoint((mouse_pos[0], mouse_pos[1])):
            rewards_scene.scrollbar.set_pos(pygame.mouse.get_pos()[0] - rewards_scene.scrollbar.get_width() / 2,
                                            rewards_scene.scrollbar.rect.y)
            
    # Home button
    helper.button_pressed(rewards_scene.get_home_button())

    
def pause() -> None:
    """
    Affiche la scène de pause
    """
    pause_scene.draw(screen)
    
    helper.button_pressed(pause_scene.homepage_button)
    helper.button_pressed(pause_scene.resume_button)
    helper.button_pressed(pause_scene.restart_button)
    helper.button_pressed(pause_scene.quit_button)
    

def score() -> None:
    """
    Affiche la scène du score
    """
    ...
    
def splash_screen() -> None:
    """
    Affiche la scène d'accueil
    """
    splash_screen_scene.draw(screen)
    
    helper.button_pressed(splash_screen_scene.start_button)
    helper.button_pressed(splash_screen_scene.rewards_button)
    helper.button_pressed(splash_screen_scene.quit_button)
    
def settings() -> None:
    """
    Affiche la scène de paramètre
    """
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
        case GameState.SPLASH_SCREEN:
            splash_screen()
        case GameState.SETTINGS:
            settings()

    clock.tick(240)

    # Update the screen
    pygame.display.flip()
    pygame.display.update()
