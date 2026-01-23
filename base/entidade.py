import math

import pygame

from base.transform import Transform
from dados.configuracao import tamanho_dos_tiles, altura_hexagono, largura_hexagono
from dados.texto_debug import TextoDebug


class Entidades:
    def __init__(self,
                 tamanho: tuple[int,int] = [largura_hexagono+2, altura_hexagono+4],
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
        pass

    def foi_clicado(self, botao):
       # print("EU FUI CLICACDO COM O BOTAO ", botao)

        pass


