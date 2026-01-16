import pygame
from dados.configuracao import tamanho_dos_tiles
from dados.cores import *
from base.transform import Transform
from base.entidade import Entidades

import math

class Tile(Transform, Entidades):
    def __init__(self, tabuleiro_pai, posicao_array, cor_tile, posicao, altura: int = 0, tipo: str = "chao", ancora: None = None):
        super().__init__(posicao=posicao, altura=altura, tamanho=(tamanho_dos_tiles, tamanho_dos_tiles + tamanho_dos_tiles/2), ancora=ancora)

        self.tipo = tipo if tipo else "chao"
        self.tabuleiro_pai = tabuleiro_pai
        self.posicao_array = posicao_array

        self.pontos = []
        self.pontos_parede = []

        self.pontos_hexagono()

        if posicao_array[1]%3 == 0:
            self.cor = cor[cor_tile][0]
            self.cor_borda = gerar_cor_borda(cor[cor_tile][0])

        elif posicao_array[1]%3 == 1:
            self.cor = cor[cor_tile][1]
            self.cor_borda = gerar_cor_borda(cor[cor_tile][1])

        elif posicao_array[1]%3 == 2:
            self.cor = cor[cor_tile][2]
            self.cor_borda = gerar_cor_borda(cor[cor_tile][2])





    def pontos_hexagono(self):

        largura = self.surface.get_width()
        altura = self.surface.get_height()

        centro_x = largura / 2 -0.7
        centro_y = altura / 2

        raio = (largura / 2) - 0.5

        for i in range(6):
            angulo_radiano = math.radians(i * 60)

            x = centro_x + raio * math.cos(angulo_radiano)
            y = centro_y + raio * math.sin(angulo_radiano)
            self.pontos.append((x, y))

    def desenhar_hexagono(self):
        if not self.pontos_parede:

            altura_muro = 30

            self.pontos_parede = [
                self.pontos[0],
                self.pontos[1],
                self.pontos[2],
                self.pontos[3],
                (self.pontos[3][0], self.pontos[3][1]+altura_muro),
                (self.pontos[2][0], self.pontos[2][1] + altura_muro),
                (self.pontos[1][0], self.pontos[1][1] + altura_muro),
                (self.pontos[0][0], self.pontos[0][1] + altura_muro)
            ]

        pygame.draw.polygon(self.surface, self.cor, self.pontos, 0)
        pygame.draw.polygon(self.surface, gerar_cor_borda(self.cor), self.pontos_parede, 0)






    def vizinho(self, vizinho):

        x,y = self.posicao_array
        mapa = self.tabuleiro_pai.mapa

        if vizinho == "baixo":
            novo_y = y +2

            if 0 < novo_y < len(mapa):
                return (mapa[self.posicao_array[1]+2][self.posicao_array[0]])

        return None

