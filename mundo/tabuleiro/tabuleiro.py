from .tiles import Tile
from .mapas import mapa, converter_mapa
from base.transform import Transform

class Tabuleiro(Transform):

    def __init__(self, posicao, altura, mapa_base, cor_tile):
        self.cor_tile = cor_tile
        self.mapa_base = mapa[mapa_base]
        self.mapa = []
        self.tamanho = (len(self.mapa_base[0]), len(self.mapa_base))

        super().__init__(posicao=posicao, altura=altura)



        for Y, coluna in enumerate(self.mapa_base):
            linha = []

            for X, casa in enumerate(coluna):
                linha.append(Tile(  tabuleiro_pai= self,
                                    cor_tile= self.cor_tile,
                                    posicao_array= (X,Y),
                                    posicao= (X, Y),
                                    altura= casa[1],
                                    tipo=  converter_mapa(casa[0]),
                                    ancora=self))

            self.mapa.append(linha)


        for coluna in self.mapa:
            for tile in coluna:
               if tile.tipo == "chao":
                   tile.desenhar_hexagono()



    def esta_no_tabuleiro(self, posicao_checada, altura):

        if altura != self.altura:
            return False

        x, y = posicao_checada
        x0, y0 = self.posicao_mundo_tile
        horizontal, vertical = self.tamanho

        if x0 <= x < x0  + horizontal and y0 <= y < y0 + vertical:
            return True

        else:
            return False







