import pygame
from tiles import criar_tiles
from variaveis_globais import tamanho_dos_tiles


mapas = [
    [
        [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
        [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
        [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
        [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]],
        [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
    ],

    [
        [[1,1],[1,1],[1,1]],
        [[1,1],[1,1],[1,1]],
        [[1,1],[1,1],[1,1]],
        [[1,1],[1,1],[1,1]],
        [[1,1],[1,1],[1,1]]
    ],

    [
        [[0,1],[1,1],[0,1]],
        [[1,1],[1,1],[1,1]],
        [[0,1],[1,1],[0,1]]
    ]
]




def criar_tabuleiro(posicao, tipo, cor):

    posicao_tabuleiro = (posicao[0]*(tamanho_dos_tiles+1), posicao[1]*(tamanho_dos_tiles+1))

    tiles = criar_tiles(cor)

    mapa = mapas[tipo]

    tabuleiro_surface = pygame.Surface(
        (
             len(mapa[0])*(tamanho_dos_tiles+1),
            len(mapa)*(tamanho_dos_tiles+1) + tamanho_dos_tiles/2
        ),
        pygame.SRCALPHA
    )


    for Y, linha in enumerate(mapa):
        for X, tile in enumerate(linha):
            if tile[0] == 1:
                tabuleiro_surface.blit(
                    tiles,
                    ((tamanho_dos_tiles+1) * X,
                     (tamanho_dos_tiles +1) * Y)
                )



    return  tabuleiro_surface, posicao_tabuleiro


