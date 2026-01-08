from .tiles import Tile
from .mapas import mapa, converter_mapa
from base.transform import Transform

class Tabuleiro(Transform):

    def __init__(self, posicao, altura, mapa_base, cor_tile):
        self.cor_tile = cor_tile
        self.mapa_base = mapa[mapa_base]
        self.mapa = []

        super().__init__(posicao=posicao, altura=altura)



        for X, linha in enumerate(self.mapa_base):
            coluna = []

            for Y, casa in enumerate(linha):
                coluna.append(Tile( cor_tile= self.cor_tile,
                                    posicao= (X, Y),
                                    altura= casa[1],
                                    tipo=  converter_mapa(casa[0]),
                                    ancora=self))

            self.mapa.append(coluna)



    def printar_mapa(self):
        print(self.mapa)







