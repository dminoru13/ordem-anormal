import pygame
from .tiles import tile
from variaveis_globais import *
from .mapas import mapa, converter_mapa


class tabuleiro:
    def __init__(self, posicao_tabuleiro, altura, mapa_base, cor_tile):
        self.posicao = (posicao_tabuleiro[0] * tamanho_dos_tiles, posicao_tabuleiro[1] * tamanho_dos_tiles - altura*tamanho_dos_tiles/2)
        self.altura = altura
        self.cor_tile = cor_tile
        self.mapa_base = mapa[mapa_base]

        self.mapa = []

        for X, linha in enumerate(self.mapa_base):
            coluna = []

            for Y, casa in enumerate(linha):
                coluna.append(tile(self.cor_tile, (X*tamanho_dos_tiles, Y*tamanho_dos_tiles - casa[1]*tamanho_dos_tiles/2 + self.altura*tamanho_dos_tiles/2), casa[1], converter_mapa(casa[0])))

            self.mapa.append(coluna)

        self.surface = pygame.Surface(
            (
                len(self.mapa[0]) * tamanho_dos_tiles,
                len(self.mapa) * tamanho_dos_tiles + tamanho_dos_tiles / 2 + altura*tamanho_dos_tiles/2
            ),
            pygame.SRCALPHA
        )




    def desenhar(self, tela):

        for Y, linha in enumerate(self.mapa):
            for X, casa in enumerate(linha):
                casa.desenhar(self.surface)


        tela.blit(self.surface, self.posicao)

    def alterar_mapa(self, cordenadas, estado):
        self.cordenadas = cordenadas
        self.estado = estado







