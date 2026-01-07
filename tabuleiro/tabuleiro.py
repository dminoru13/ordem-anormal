import pygame
from .tiles import tile
from variaveis_globais import *
from .mapas import mapa


class tabuleiro:
    def __init__(self, posicao_tabuleiro, mapa_base, cor1, cor2: tuple | None = None):
        self.posicao = (posicao_tabuleiro[0] * tamanho_dos_tiles, posicao_tabuleiro[1] * tamanho_dos_tiles)

        self.cor1 = cor1
        self.cor2 = cor2
        self.mapa_base = mapa[mapa_base]
        self.tile1 = tile(cor[self.cor1])
        self.tile2 = tile(cor[self.cor2]) if cor2 else None

        self.mapa = []

        for X, linha in enumerate(self.mapa_base):
            coluna = []

            for Y, casa in enumerate(linha):
                coluna.append(tile(cor[cor1]))

            self.mapa.append(coluna)

        self.surface = pygame.Surface(
            (
                len(self.mapa[0]) * tamanho_dos_tiles,
                len(self.mapa) * tamanho_dos_tiles + tamanho_dos_tiles / 2
            ),
            pygame.SRCALPHA
        )




    def desenhar(self, tela):

        for Y, linha in enumerate(self.mapa):
            for X, casa in enumerate(linha):
                self.surface.blit(casa.surface, (X * tamanho_dos_tiles, Y * tamanho_dos_tiles))


        tela.blit(self.surface, self.posicao)

    def alterar_mapa(self, cordenadas, estado):
        self.cordenadas = cordenadas
        self.estado = estado







