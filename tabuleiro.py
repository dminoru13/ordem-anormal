import pygame
from tiles import criar_tiles, tamanho_dos_tiles






def criar_tabuleiro(posicao, tamanho_horizontal_tabuleiro, tamanho_vertical_tabuleiro, cor):

    posicao_tabuleiro = posicao

    tiles = criar_tiles(cor)

    tabuleiro_surface = pygame.Surface(
        (
            tamanho_horizontal_tabuleiro*(tamanho_dos_tiles+1),
            tamanho_vertical_tabuleiro*(tamanho_dos_tiles+1) + tamanho_dos_tiles/2
        ),
        pygame.SRCALPHA
    )


    for Y in range(tamanho_vertical_tabuleiro):
        for X in range(tamanho_horizontal_tabuleiro):
            tabuleiro_surface.blit(
                tiles,
                ((tamanho_dos_tiles+1) * X,
                 (tamanho_dos_tiles +1) * Y)
            )



    return  tabuleiro_surface, posicao_tabuleiro