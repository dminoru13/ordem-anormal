import pygame
from dados.configuracao import tamanho_dos_tiles
from base.transform import Transform
from base.entidade import Entidades


class Peca(Transform, Entidades):
    def __init__(self, nome, posicao, altura):
        super().__init__(posicao=posicao, altura=altura, clicavel=True, tamanho=(tamanho_dos_tiles,tamanho_dos_tiles))
        self.nome = nome
        pygame.draw.circle(self.surface, (200, 50, 50), (tamanho_dos_tiles / 2, tamanho_dos_tiles / 2),tamanho_dos_tiles*0.7 / 2)

    def foi_clicado(self, botao):
        pass


    def estou_no_tabuleiro(self, tabuleiro):
        print(tabuleiro.esta_no_tabuleiro(self.posicao_mundo_tile, self.altura))
