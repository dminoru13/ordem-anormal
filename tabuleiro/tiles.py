import pygame
from variaveis_globais import tamanho_dos_tiles

class tile:
    def __init__(self, cor, altura: int | None = None, estado: str | None = None):
        self.surface = pygame.Surface((tamanho_dos_tiles, tamanho_dos_tiles*1.5), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()

        self.cor = cor
        self.altura = altura if altura else 0
        self.estado = estado if estado else ""

        pygame.draw.rect(self.surface, self.cor, (0, 0, tamanho_dos_tiles, tamanho_dos_tiles))

        sombra = (self.cor[0] //2, self.cor[1]//2, self.cor[2]//2)
        pygame.draw.rect(self.surface, sombra, (0, tamanho_dos_tiles, tamanho_dos_tiles, tamanho_dos_tiles / 2))

