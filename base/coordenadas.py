import pygame
from variaveis_globais import *


class Coordenadas:
    def __init__(self,
                 posicao,
                 altura,
                 tamanho: tuple[int,int] = [tamanho_dos_tiles, tamanho_dos_tiles],
                 tabuleiro: int | None = None,
                 clicavel: bool = False
                 ):





        self.posicao = (posicao[0]*tamanho_dos_tiles, posicao[1]*tamanho_dos_tiles - altura*tamanho_dos_tiles/2)
        self.altura = altura
        self.tabuleiro = tabuleiro
        self.tamanho = tamanho if tamanho else (1,1)
        self.surface = pygame.Surface(tamanho, pygame.SRCALPHA)
        self.rect = self.surface.get_rect()
        self.rect.topleft = self.posicao
        self.clicavel = clicavel

    def desenhar(self, tela):
        self.rect.topleft = self.posicao
        tela.blit(self.surface, self.posicao)



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
