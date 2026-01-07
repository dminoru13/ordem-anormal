from variaveis_globais import *

class peca:
    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao
        self.surface = pygame.Surface((tamanho_dos_tiles, tamanho_dos_tiles), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()

        rect = self.surface.get_rect()

        pygame.draw.circle(self.surface, (200, 50, 50), (tamanho_dos_tiles / 2, tamanho_dos_tiles / 2),
                           tamanho_dos_tiles / 2)

    def desenhar(self, tela):
        pos_peca = tuple(valor * 32 for valor in self.posicao)
        self.rect.topleft = pos_peca
        tela.blit(self.surface, self.rect)

    def foi_clicado(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)