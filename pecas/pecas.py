from variaveis_globais import *

class peca:
    def __init__(self, nome, posicao, altura):
        self.nome = nome
        self.posicao = posicao
        self.altura = altura
        self.surface = pygame.Surface((tamanho_dos_tiles, tamanho_dos_tiles), pygame.SRCALPHA)
        self.rect = self.surface.get_rect()

        rect = self.surface.get_rect()

        pygame.draw.circle(self.surface, (200, 50, 50), (tamanho_dos_tiles / 2, tamanho_dos_tiles / 2),tamanho_dos_tiles / 2)

    def desenhar(self, tela):
        pos_peca = (self.posicao[0] * tamanho_dos_tiles, self.posicao[1] * tamanho_dos_tiles - self.altura * tamanho_dos_tiles/2)
        self.rect.topleft = pos_peca
        tela.blit(self.surface, self.rect)

    def foi_clicado(self, pos_mouse, qual_botao):
        if qual_botao == 1:
            for x in range(4):
                return self.rect.collidepoint(pos_mouse)