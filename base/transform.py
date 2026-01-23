from __future__ import annotations
import pygame
from dados.configuracao import tamanho_dos_tiles, altura_hexagono, largura_hexagono,raio_hexagono



class Transform:
    def __init__(self,
                 posicao,
                 altura,
                 ancora: Transform | None = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)


        self.posicao_pixel = (posicao[0]*(largura_hexagono - (largura_hexagono-raio_hexagono)/2), posicao[1]*altura_hexagono - altura*altura_hexagono/2)
        self.posicao_tile = posicao
        self.altura = altura
        self.ancora = ancora

    @property
    def posicao_mundo_pixel(self):
        if self.ancora:
            ax, ay = self.ancora.posicao_mundo_pixel
            x, y = self.posicao_pixel
            return x + ax, y + ay
        return self.posicao_pixel

    @property
    def posicao_mundo_tile(self):
        if self.ancora:
            ax, ay = self.ancora.posicao_mundo_tile
            x, y = self.posicao_tile
            return x + ax, y + ay
        return self.posicao_tile



