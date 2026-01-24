import pygame
from dados.configuracao import largura_hexagono, altura_hexagono,raio_hexagono
from base.transform import Transform
from base.entidade import Entidades


class Peca(Transform, Entidades):
    def __init__(self, nome, posicao, altura, tabuleiro):
        super().__init__(posicao=posicao, altura=altura, clicavel=True, tamanho=(largura_hexagono,altura_hexagono), ancora=tabuleiro)
        self.nome = nome
        pygame.draw.circle(self.surface, (200, 50, 50), (largura_hexagono / 2, altura_hexagono / 2),raio_hexagono*0.7)

    def foi_clicado(self, botao):
        pass


    def estou_no_tabuleiro(self, tabuleiro):
        print(tabuleiro.esta_no_tabuleiro(self.posicao_mundo_tile, self.altura))
