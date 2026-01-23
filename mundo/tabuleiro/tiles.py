import pygame
from dados.configuracao import raio_hexagono, altura_hexagono, largura_hexagono
from dados.cores import *
from base.transform import Transform
from base.entidade import Entidades
import math


class Tile(Transform, Entidades):
    def __init__(self,  tabuleiro_pai, posicao_array, cor_tile, posicao, altura: int = 0, tipo: str = "chao", ancora: None = None):

        super().__init__(posicao=posicao, altura=altura, ancora=tabuleiro_pai)

        self.tipo = tipo if tipo else "chao"
        self.tabuleiro_pai = tabuleiro_pai
        self.posicao_array = posicao_array

        self.pontos = []
        self.pontos_parede = []

        self.pontos_hexagono()

        self.debug_texto.mudar_texto(self.posicao_array)

        self.cor = cor[cor_tile][0]
        self.cor_borda = gerar_cor_borda(cor[cor_tile][0])

        self.pontos_hexagono()
        self.desenhar_hexagono()




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

        pygame.draw.polygon(self.surface, self.cor, self.pontos)
        pygame.draw.polygon(self.surface, self.cor_borda, self.pontos, 2)



    VIZINHOS = [
        (+1,  0),
        (+1, -1),
        ( 0, -1),
        (-1,  0),
        (-1, +1),
        ( 0, +1),
    ]










