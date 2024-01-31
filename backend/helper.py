import pygame

from elements.button import Button

def button_pressed(button: Button) -> bool:
    """
    Vérifie si un bouton (Button) à été appuyé
    :param bouton (Button): Le bouton à vérifier
    :return (bool): True si le bouton à été appuyé. Sinon, False
    """
    if pygame.mouse.get_pressed()[0]:
        mouse_pos = pygame.mouse.get_pos()
        home_button_pos = button.get_rect()
        if home_button_pos[0] <= mouse_pos[0] <= home_button_pos[0] + home_button_pos[2] and \
            home_button_pos[1] <= mouse_pos[1] <= home_button_pos[1] + home_button_pos[3]:
            button.perform_action()