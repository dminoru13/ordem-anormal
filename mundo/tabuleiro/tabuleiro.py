from .tiles import Tile
from variaveis_globais import *
from .mapas import mapa
from base.coordenadas import Coordenadas


class Tabuleiro(Coordenadas):

    _contador_id = 0

    def __init__(self, posicao, altura, mapa_base, cor_tile):
        self.id = self._contador_id
        Tabuleiro._contador_id += 1
        self.cor_tile = cor_tile
        self.mapa_base = mapa[mapa_base]
        self.mapa = []
        self.alturatemporaria = altura

        for X, linha in enumerate(self.mapa_base):
            coluna = []

            for Y, casa in enumerate(linha):
                coluna.append(Tile( cor_tile= self.cor_tile, posicao=(posicao[0] + X, posicao[1] + Y), posicao_no_tabuleiro=(X,Y), altura=[1], tipo=(casa[0]), tabuleiro=self.id))

            self.mapa.append(coluna)

        tamanho = (len(self.mapa[0]) * tamanho_dos_tiles,len(self.mapa) * tamanho_dos_tiles + tamanho_dos_tiles / 2 + altura * tamanho_dos_tiles / 2)

        super().__init__(posicao=posicao,altura=altura, tamanho=tamanho, clicavel=False)


    def desenhar(self, tela):
        for linha in self.mapa:
            for tile in linha:
                tile.desenhar(tela)

    def foi_clicado(self, botao):
        print(self.id)






    def printar_mapa(self):
        print(self.mapa)







