import pygame

from base.transform import Transform
from dados.configuracao import tamanho_dos_tiles


class Entidades:
    def __init__(self,
                 tamanho: tuple[int,int] = [tamanho_dos_tiles, tamanho_dos_tiles],
                 clicavel: bool = False,
                 **kwargs
                 ):
        super().__init__(**kwargs)




        self.tamanho = tamanho if tamanho else (1,1)
        self.surface = pygame.Surface(tamanho, pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.clicavel = clicavel

    def desenhar(self, tela, transform: Transform | None = None):
        if transform is None:
            transform = self
        self.rect.topleft = transform.posicao_mundo
        tela.blit(self.surface, transform.posicao_mundo)



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
