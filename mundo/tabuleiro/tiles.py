import pygame
from dados.configuracao import tamanho_dos_tiles, raio_hexagono
from dados.cores import *
from base.transform import Transform
from base.entidade import Entidades
import math


class Tile(Transform, Entidades):
    def __init__(self,  tabuleiro_pai, posicao_array, cor_tile, posicao_axial, altura: int = 0, tipo: str = "chao", ancora: None = None):

        largura = int(2 * raio_hexagono)
        altura_surf = int(math.sqrt(3) * raio_hexagono)
        tamanho_surf = (largura, altura_surf)



        super().__init__(posicao=posicao_axial, altura=altura, tamanho=tamanho_surf, ancora=tabuleiro_pai)

        self.tipo = tipo if tipo else "chao"
        self.tabuleiro_pai = tabuleiro_pai
        self.posicao_array = posicao_array

        self.pontos = []
        self.pontos_parede = []

        self.pontos_hexagono()

        self.debug_texto.mudar_texto(self.posicao_array)

        self.cor = cor[cor_tile][0]
        self.cor_borda = gerar_cor_borda(cor[cor_tile][0])




    def pontos_hexagono(self):

        largura = self.surface.get_width()
        altura = self.surface.get_height()

        centro_x = largura / 2
        centro_y = altura / 2

        self.pontos = []

        for i in range(6):
            angulo = math.radians(60 * i)
            x = centro_x + raio_hexagono * math.cos(angulo)
            y = centro_y + raio_hexagono * math.sin(angulo)
            self.pontos.append((x, y))

    def desenhar_hexagono(self):
        if not self.pontos_parede:

            altura_muro = 30

            self.pontos_parede = [*self.pontos]

        pygame.draw(self.surface, self.cor, self.pontos, 0)
        pygame.draw(self.surface, gerar_cor_borda(self.cor), self.pontos, 0)


        pygame.draw.polygon(self.surface, self.cor, self.pontos, 0)
        pygame.draw.polygon(self.surface, gerar_cor_borda(self.cor), self.pontos_parede, 0)



VIZINHOS = [
    (+1,  0),
    (+1, -1),
    ( 0, -1),
    (-1,  0),
    (-1, +1),
    ( 0, +1),
]









