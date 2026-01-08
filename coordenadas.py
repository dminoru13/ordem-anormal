import pygame
from variaveis_globais import *


class Coordenadas:
    def __init__(self, posicao, altura, tamanho: tuple[int,int] = [tamanho_dos_tiles, tamanho_dos_tiles], tabuleiro: int | None = None):
        self.posicao = (posicao[0]*tamanho_dos_tiles, posicao[1]*tamanho_dos_tiles - altura*tamanho_dos_tiles/2)
        self.altura = altura
        self.tabuleiro = tabuleiro
        self.tamanho = tamanho if tamanho else (1,1)
        self.surface = pygame.Surface(tamanho, pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.posicao

    def desenhar(self, tela):
        tela.blit(self.surface, self.posicao)
