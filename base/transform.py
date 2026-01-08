from __future__ import annotations
import pygame
from dados.configuracao import tamanho_dos_tiles



class Transform:
    def __init__(self,
                 posicao,
                 altura,
                 ancora: Transform | None = None,
                 **kwargs
                 ):
        super().__init__(**kwargs)


        self.posicao = (posicao[0]*tamanho_dos_tiles, posicao[1]*tamanho_dos_tiles - altura*tamanho_dos_tiles/2)
        self.altura = altura
        self.ancora = ancora

    @property
    def posicao_mundo(self):
        if self.ancora:
            ax, ay = self.ancora.posicao_mundo
            x, y = self.posicao
            return x + ax, y + ay
        return self.posicao



