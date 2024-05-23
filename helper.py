"""
Fichier regrouppant différentes fonction utiles au programme

@Author: Soren
"""

import pygame


def load_image(path: str) -> pygame.Surface:
    """Charger une image avec pygame depuis un chemin

    Args:
        path (str): Chemin de l'image

    Returns:
        pygame.Surface: L'image mise en paramètre
    """
    return pygame.image.load(path)
