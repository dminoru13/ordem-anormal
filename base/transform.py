from __future__ import annotations

import math

import pygame
from dados.configuracao import tamanho_dos_tiles, raio_hexagono


def axial_para_pixel(q, r):

    x = raio_hexagono * 3 / 2 * r
    y = raio_hexagono * math.sqrt(3) * (q + r / 2)

    return x, y

def pixel_para_axial( x, y):

    q = (2/3 * x) / raio_hexagono
    r = (-1/3 * x + math.sqrt(3)/3 * y)/ raio_hexagono
    return 0

def arredondar_axial( qf, rf):

    xf = qf
    zf = rf
    yf = -xf -zf

    xr = round(xf)
    yr = round(yf)
    zr = round(zf)

    x_diff = abs(xr - xf)
    y_diff = abs(yr - yf)
    z_diff = abs(zr - zf)

    if x_diff > y_diff and x_diff > z_diff:
        xr = -yr - zr
    elif y_diff > z_diff:
        yr = -xr - zr
    else:
        zr = -xr - yr

    return int(xr), int(zr)



class Transform:
    def __init__(self, posicao, altura, ancora: Transform | None = None, **kwargs):
        super().__init__(**kwargs)

        self.q, self.r = posicao
        self.altura = altura
        self.ancora = ancora
        self.posicao_pixel = axial_para_pixel(self.q, self.r)

    @property
    def posicao_mundo_pixel(self):
        x, y = axial_para_pixel(self.q, self.r)

        y -= self.altura * (raio_hexagono * 0.5)

        if self.ancora:
            ax, ay = self.ancora.posicao_mundo_pixel
            return (x + ax, y + ay)
        return (x, y)

    @property
    def posicao_mundo_tile(self):
        if self.ancora:
            ax, ay = self.ancora.posicao_mundo_tile
            return (self.q + ax, self.r + ay)
        return (self.q, self.r)







