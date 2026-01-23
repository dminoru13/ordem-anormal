from random import choice

import pygame
from dados.configuracao import raio_hexagono, altura_hexagono, largura_hexagono
from dados.cores import *
from base.transform import Transform
from base.entidade import Entidades
import math
import random


class Tile(Transform, Entidades):
    def __init__(self,  tabuleiro_pai, posicao_array, cor_tile, posicao, altura: int = 0, tipo: str = "chao", ancora: None = None):

        self.tamanho = (largura_hexagono+2, altura_hexagono + 4 + (altura+1) * (altura_hexagono/2))

        super().__init__(posicao=posicao,tamanho=self.tamanho, altura=altura, ancora=tabuleiro_pai)



        self.tipo = tipo if tipo else "chao"
        self.tabuleiro_pai = tabuleiro_pai
        self.posicao_array = posicao_array

        self.pontos = []
        self.pontos_parede = []

        self.pontos_hexagono()

        self.debug_texto.mudar_texto(self.posicao_array)

        self.cor = cor[cor_tile][self.posicao_tile[1]%3]
        self.cor_borda = (180, 70, 100)
        self.cor_parede = (100, 100, 100)

        #self.surface.fill((255,255,0))

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
            x = centro_x + raio_hexagono * math.cos(angulo) -1
            y = centro_y + raio_hexagono * math.sin(angulo) - (self.altura+1) * altura_hexagono/4
            self.pontos.append((x, y))

    def desenhar_hexagono(self):
        if not self.pontos_parede:

            altura_muro = (self.altura+1) * altura_hexagono/2

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

            self.pontos_parede_auxiliar = [
                self.pontos[1],
                self.pontos[2],
                (self.pontos[2][0], self.pontos[2][1] + altura_muro-1),
                (self.pontos[1][0], self.pontos[1][1] + altura_muro-1),
            ]

        pygame.draw.polygon(self.surface, self.cor, self.pontos)
        pygame.draw.polygon(self.surface, self.cor_parede, self.pontos_parede)

        pygame.draw.polygon(self.surface, (min(self.cor_parede[0] + 10, 255), min(self.cor_parede[0] + 10, 255), min(self.cor_parede[0] + 10, 255)), self.pontos_parede_auxiliar)

        pygame.draw.polygon(self.surface, self.cor_borda, self.pontos, 1)






    def evento(self, evento):

        self.rect.topleft = self.posicao_mundo_pixel

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                if self.rect.collidepoint(evento.pos):
                    print(self.altura)










