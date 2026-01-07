import pygame
from .tiles import criar_tiles
from variaveis_globais import tamanho_dos_tiles
from .mapas import mapas






def criar_tabuleiro(posicao, tipo, cor, cor2: tuple | None = None):

    posicao_tabuleiro = (posicao[0]*(tamanho_dos_tiles), posicao[1]*(tamanho_dos_tiles))

    mapa = mapas[tipo]

    tabuleiro_surface = pygame.Surface(
        (
             len(mapa[0])*(tamanho_dos_tiles),
            len(mapa)*(tamanho_dos_tiles) + tamanho_dos_tiles/2
        ),
        pygame.SRCALPHA
    )

    tiles1 = criar_tiles(cor)

    if cor2 is None:
        for Y, linha in enumerate(mapa):
            for X, tile in enumerate(linha):
                if tile[0] == 1:
                    tabuleiro_surface.blit(
                        tiles1,
                        ((tamanho_dos_tiles) * X,
                         (tamanho_dos_tiles ) * Y)
                    )

    if cor2 is not None:
        tiles2 = criar_tiles(cor2)

        for Y, linha in enumerate(mapa):
            for X, tile in enumerate(linha):
                if tile[0] == 1:
                    if Y % 2 == 1:
                        if X % 2 == 0:
                            tabuleiro_surface.blit(
                                tiles1,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )
                        else:
                            tabuleiro_surface.blit(
                                tiles2,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )
                    else:
                        if X % 2 == 0:
                            tabuleiro_surface.blit(
                                tiles2,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )
                        else:
                            tabuleiro_surface.blit(
                                tiles1,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )




    return  tabuleiro_surface, posicao_tabuleiro



cor = [
    # 0 – claro
    (240, 217, 181),  # bege clássico

    # 1 – escuro
    (100, 10, 0),  # vermelho escuro queimado

    # 2 – claro
    (225, 235, 220),  # verde pálido

    # 3 – escuro
    (70, 102, 85),  # verde musgo

    # 4 – claro
    (230, 230, 230),  # cinza claro

    # 5 – escuro
    (60, 60, 60),  # cinza carvão

    # 6 – claro
    (235, 222, 189),  # pergaminho

    # 7 – escuro
    (120, 90, 50),  # marrom escuro

    # 8 – claro
    (210, 225, 240),  # azul gelo

    # 9 – escuro
    (30, 45, 80),  # azul marinho

    # 10 – claro
    (245, 245, 220),  # creme

    # 11 – escuro
    (80, 20, 20),  # vinho escuro
]
