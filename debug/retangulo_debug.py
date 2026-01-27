import pygame

from base.transform import Transform
from base.entidade import Entidades
from base.configuracao import config

class Retangulo_debug(Transform, Entidades):
    def __init__(self, posicao, cor = (255, 0, 0), tamanho = (config.largura_hexagono, config.altura_hexagono)):
        super().__init__(posicao=posicao, altura=0, clicavel=True, tamanho=(config.largura_hexagono, config.altura_hexagono))
        self.escala_anterior = config.tamanho_dos_tiles

        self.cor = cor

        self.tamanho = tamanho



    def desenhar(self, tela, transform: Transform | None = None):
        self.atualizar_escala()
        self.surface.fill(self.cor)
        super().desenhar(tela, transform)

    def atualizar_escala(self):
        if self.escala_anterior == config.tamanho_dos_tiles:
            return

        self.surface = pygame.Surface((config.largura_hexagono, config.altura_hexagono), pygame.SRCALPHA)


    def foi_clicado(self, botao):
        pass
