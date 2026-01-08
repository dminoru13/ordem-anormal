from variaveis_globais import *
from coordenadas import Coordenadas

class Peca(Coordenadas):
    def __init__(self, nome, posicao, altura):
        super().__init__(posicao, altura, clicavel=True)
        self.nome = nome
        pygame.draw.circle(self.surface, (200, 50, 50), (tamanho_dos_tiles / 2, tamanho_dos_tiles / 2),tamanho_dos_tiles*0.7 / 2)

    def foi_clicado(self, botao):
        print(f"EU, {self.nome}, FUI CLICACDO COM O BOTAO ", botao)