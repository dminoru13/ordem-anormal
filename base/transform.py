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

        self.altura = altura

        largura_geometrica = (largura_hexagono - (largura_hexagono-raio_hexagono)/2)
        altura_geometrica = altura_hexagono
        x = posicao[0]
        y = posicao[1]



        self.posicao_pixel = ( x *  largura_geometrica, (y + (x%2)/2) * altura_geometrica - self.altura*altura_hexagono/2)




        self.posicao_tile = posicao
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

    @property
    def posicao_mundo_pixel_sem_altura(self):
        largura_geometrica = (largura_hexagono - (largura_hexagono - raio_hexagono) / 2)
        altura_geometrica = altura_hexagono
        x = self.posicao_tile[0]
        y = self.posicao_tile[1]

        return  (x * largura_geometrica, (y + (x % 2) / 2) * altura_geometrica)



