from __future__ import annotations
import pygame
from dados.configuracao import altura_hexagono, largura_hexagono,raio_hexagono
import camera



class Transform:
    def __init__(self,
                 posicao,
                 altura,
                 ancora: Transform | None = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)

        self.altura = altura

        self.largura_geometrica = (largura_hexagono - (largura_hexagono-raio_hexagono)/2)
        self.altura_geometrica = altura_hexagono
        self.x = posicao[0]
        self.y = posicao[1]








        self.posicao_tile = posicao
        self.ancora = ancora

    @property
    def posicao_pixel(self):
        x, y = self.posicao_tile
        return(
            (x * self.largura_geometrica,
            (y + (self.x % 2) / 2) * self.altura_geometrica - self.altura * altura_hexagono / 2)
        )

    @property
    def posicao_mundo_pixel(self):
        if self.ancora:
            ax, ay = self.ancora.posicao_mundo_pixel
            x, y = self.posicao_pixel
            return x + ax, y + ay
        return (self.posicao_pixel[0]  + camera.camera_x, self.posicao_pixel[1] +  + camera.camera_y)


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
