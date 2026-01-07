import pygame
from variaveis_globais import  *

def criar_pecas():

    peca_surface = pygame.Surface(
        (tamanho_dos_tiles, tamanho_dos_tiles),
        pygame.SRCALPHA
    )

    rect = peca_surface.get_rect()

    pygame.draw.circle(peca_surface, (200, 50, 50), (tamanho_dos_tiles/2, tamanho_dos_tiles/2), tamanho_dos_tiles/2)

    return peca_surface, rect

