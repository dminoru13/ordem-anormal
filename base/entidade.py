import math

import pygame

from base.transform import Transform
from dados.configuracao import tamanho_dos_tiles, altura_hexagono, largura_hexagono
from dados.texto_debug import TextoDebug


class Entidades:
    def __init__(self,
                 tamanho: tuple[int,int] = [largura_hexagono, altura_hexagono],
                 clicavel: bool = False,
                 **kwargs
                 ):
        super().__init__(**kwargs)


        self.tamanho = tamanho if tamanho else (1,1)
        self.surface = pygame.Surface(tamanho, pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.clicavel = clicavel

        self.debug_texto = TextoDebug ( tela= self.surface, posicao=(0,0))



    def desenhar(self, tela, transform: Transform | None = None):
        if transform is None:
            transform = self
        self.rect.topleft = transform.posicao_mundo_pixel
        tela.blit(self.surface, transform.posicao_mundo_pixel)

        self.debug_texto.desenhar_texto()






    def evento(self, evento):
        if not self.clicavel:
            return False

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(evento.pos):
                self.foi_clicado(evento.button)
                return True
            return False

    def foi_clicado(self, botao):
        print("EU FUI CLICACDO COM O BOTAO ", botao)


