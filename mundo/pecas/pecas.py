import pygame
from base.configuracao import config
from base.transform import Transform
from base.entidade import Entidades


class Peca(Transform, Entidades):
    def __init__(self, nome, posicao, altura, tabuleiro):
        super().__init__(posicao=posicao, altura=altura, clicavel=True, tamanho=(config.largura_hexagono,config.altura_hexagono), ancora=tabuleiro)
        self.nome = nome
        self.escala_anterior = config.tamanho_dos_tiles


        pygame.draw.circle(self.surface, (200, 50, 50), (config.largura_hexagono / 2, config.altura_hexagono / 2),config.raio_hexagono*0.7)




    def desenhar(self, tela, transform: Transform | None = None):
        self.atualizar_escala()
        super().desenhar(tela, transform)

    def atualizar_escala(self):

        if self.escala_anterior == config.tamanho_dos_tiles:
            return

        self.surface = pygame.Surface((config.largura_hexagono, config.altura_hexagono), pygame.SRCALPHA)
        pygame.draw.circle(self.surface, (200, 50, 50), (config.largura_hexagono / 2, config.altura_hexagono / 2), config.raio_hexagono * 0.7)





    def foi_clicado(self, botao):
        pass


    def estou_no_tabuleiro(self, tabuleiro):
        print(tabuleiro.esta_no_tabuleiro(self.posicao_mundo_tile, self.altura))
