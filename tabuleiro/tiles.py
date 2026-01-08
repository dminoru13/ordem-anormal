import pygame
from variaveis_globais import *

class tile:
    def __init__(self, cor_tile, posicao, altura: int | None = None, tipo: str | None = None):
        self.surface = pygame.Surface((tamanho_dos_tiles, tamanho_dos_tiles*1.5), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()

        self.cor = cor[cor_tile]
        self.cor_borda = gerar_cor_borda(cor[cor_tile])
        self.altura = altura if altura else 0
        self.tipo = tipo if tipo else "chao"
        self.posicao = posicao



        if tipo == "chao":

            pygame.draw.rect(self.surface, self.cor_borda, (0, 0, tamanho_dos_tiles, tamanho_dos_tiles))
            pygame.draw.rect(self.surface, self.cor, (1, 1, tamanho_dos_tiles-2, tamanho_dos_tiles-2))


            sombra = (self.cor[0] //2, self.cor[1]//2, self.cor[2]//2)
            sombra_borda = (self.cor_borda[0] //2, self.cor_borda[1]//2, self.cor_borda[2]//2)
            pygame.draw.rect(self.surface, sombra_borda, (0, tamanho_dos_tiles, tamanho_dos_tiles, tamanho_dos_tiles / 2))
            pygame.draw.rect(self.surface, sombra, (1, tamanho_dos_tiles, tamanho_dos_tiles-2, (tamanho_dos_tiles-2) / 2))




    def desenhar(self, tabuleiro):
        tabuleiro.blit(self.surface, self.posicao)

    def clicado(self):
        pass