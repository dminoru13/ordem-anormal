import pygame
from .tiles import criar_tiles
from variaveis_globais import *
from .mapas import mapas


class tabuleiro:
    def __init__(self, posicao_tabuleiro, mapa, cor1, cor2: tuple | None = None):
        self.posicao = (posicao_tabuleiro[0] * tamanho_dos_tiles, posicao_tabuleiro[1] * tamanho_dos_tiles)
        self.mapa = mapas[mapa]
        self.cor1 = cor1
        self.cor2 = cor2
        self.surface = pygame.Surface(
            (
                len(self.mapa[0]) * tamanho_dos_tiles,
                len(self.mapa) * tamanho_dos_tiles + tamanho_dos_tiles / 2
            ),
            pygame.SRCALPHA
        )


    def desenhar(self, tela):

        tiles1 = criar_tiles(cor[self.cor1])

        if self.cor2 is None:
            for Y, linha in enumerate(self.mapa):
                for X, tile in enumerate(linha):
                    if tile[0] == 1:
                        self.surface.blit(
                            tiles1,
                            ((tamanho_dos_tiles) * X,
                             (tamanho_dos_tiles) * Y)
                        )

        if self.cor2 is not None:
            tiles2 = criar_tiles(cor[self.cor2])

            for Y, linha in enumerate(self.mapa):
                for X, tile in enumerate(linha):
                    if tile[0] == 1:
                        if Y % 2 == 1:
                            if X % 2 == 0:
                                self.surface.blit(
                                    tiles1,
                                    ((tamanho_dos_tiles) * X,
                                     (tamanho_dos_tiles) * Y)
                                )
                            else:
                                self.surface.blit(
                                    tiles2,
                                    ((tamanho_dos_tiles) * X,
                                     (tamanho_dos_tiles) * Y)
                                )
                        else:
                            if X % 2 == 0:
                                self.surface.blit(
                                    tiles2,
                                    ((tamanho_dos_tiles) * X,
                                     (tamanho_dos_tiles) * Y)
                                )
                            else:
                                self.surface.blit(
                                    tiles1,
                                    ((tamanho_dos_tiles) * X,
                                     (tamanho_dos_tiles) * Y)
                                )

        tela.blit(self.surface, self.posicao)




