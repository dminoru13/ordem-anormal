import pygame
from .tiles import Tile
from variaveis_globais import *
from .mapas import mapa, converter_mapa
from coordenadas import Coordenadas


class Tabuleiro(Coordenadas):
    def __init__(self, posicao, altura, mapa_base, cor_tile):
        self.cor_tile = cor_tile
        self.mapa_base = mapa[mapa_base]
        self.mapa = []
        self.alturatemporaria = altura

        for X, linha in enumerate(self.mapa_base):
            coluna = []

            for Y, casa in enumerate(linha):
                coluna.append(Tile(self.cor_tile, (posicao[0] + X, posicao[1] + Y), casa[1], converter_mapa(casa[0])))

            self.mapa.append(coluna)

        tamanho = (len(self.mapa[0]) * tamanho_dos_tiles,len(self.mapa) * tamanho_dos_tiles + tamanho_dos_tiles / 2 + altura * tamanho_dos_tiles / 2)

        super().__init__(posicao=posicao,altura=altura, tamanho=tamanho)


    def desenhar(self, tela):
        for linha in self.mapa:
            for tile in linha:
                tile.desenhar(tela)






    def printar_mapa(self):
        print(self.mapa)







