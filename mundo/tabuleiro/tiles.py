import pygame
from dados.configuracao import tamanho_dos_tiles
from dados.cores import *
from base.transform import Transform
from base.entidade import Entidades

import math

class Tile(Transform, Entidades):
    def __init__(self, posicao_array, cor_tile, posicao, altura: int = 0, tipo: str = "chao", ancora: None = None):
        super().__init__(posicao=posicao, altura=altura, tamanho=(tamanho_dos_tiles, tamanho_dos_tiles + tamanho_dos_tiles/2), ancora=ancora)

        self.tipo = tipo if tipo else "chao"


        if posicao_array[1]%3 == 0:
            self.cor = cor[cor_tile][0]
            self.cor_borda = gerar_cor_borda(cor[cor_tile][0])

        if posicao_array[1]%3 == 1:
            self.cor = cor[cor_tile][1]
            self.cor_borda = gerar_cor_borda(cor[cor_tile][1])

        if posicao_array[1]%3 == 2:
            self.cor = cor[cor_tile][2]
            self.cor_borda = gerar_cor_borda(cor[cor_tile][2])



        if tipo == "chao":

           self.desenhar_hexagono()

    def desenhar_hexagono(self):

        pontos = []
        pontos_parede = []

        largura = self.surface.get_width()
        altura = self.surface.get_height()

        centro_x = largura / 2 -0.7
        centro_y = altura / 2

        raio = (largura / 2) - 0.5

        for i in range(6):
            angulo_radiano = math.radians(i * 60)

            x = centro_x + raio * math.cos(angulo_radiano)
            y = centro_y + raio * math.sin(angulo_radiano)
            pontos.append((x, y))

        pygame.draw.polygon(self.surface, self.cor, pontos, 0)

        for i in range(3):






    def aguarde(self):

        self.cor = clareamento_por_altura(self.cor, self.altura)

        pygame.draw.rect(self.surface, self.cor_borda, (0, 0, tamanho_dos_tiles, tamanho_dos_tiles))
        pygame.draw.rect(self.surface, self.cor, (1, 1, tamanho_dos_tiles - 2, tamanho_dos_tiles - 2))

        sombra = (self.cor[0] // 2, self.cor[1] // 2, self.cor[2] // 2)
        sombra_borda = (self.cor_borda[0] // 2, self.cor_borda[1] // 2, self.cor_borda[2] // 2)
        pygame.draw.rect(self.surface, sombra_borda, (0, tamanho_dos_tiles, tamanho_dos_tiles, tamanho_dos_tiles))
        pygame.draw.rect(self.surface, sombra, (1, tamanho_dos_tiles, tamanho_dos_tiles - 2, (tamanho_dos_tiles - 2)))

