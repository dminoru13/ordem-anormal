from variaveis_globais import *
from coordenadas import Coordenadas

class Peca(Coordenadas):
    def __init__(self, nome, posicao, altura):
        super().__init__(posicao, altura)
        self.nome = nome
        pygame.draw.circle(self.surface, (200, 50, 50), (tamanho_dos_tiles / 2, tamanho_dos_tiles / 2),tamanho_dos_tiles / 2)


    def foi_clicado(self, pos_mouse, qual_botao):
        if qual_botao == 1:
            for x in range(4):
                return self.rect.collidepoint(pos_mouse)