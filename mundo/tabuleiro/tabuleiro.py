from .tiles import Tile
from .mapas import mapa, converter_mapa
from base.transform import Transform

class Tabuleiro(Transform):

    def __init__(self, posicao, altura, mapa_base, cor_tile):
        super().__init__(posicao=posicao, altura=altura)

        self.tiles = {}
        self.mapa_base = mapa[mapa_base]
        self.cor_tile = cor_tile


        for r, linha in enumerate(self.mapa_base):
            for q, casa in enumerate(linha):
                tipo = converter_mapa(casa[0])
                altura_casa = casa[1]
                posicao_axial = (q, r),
                tile = Tile(tabuleiro_pai=self,
                            posicao_array=(q, r),
                            cor_tile=self.cor_tile,
                            posicao_axial=posicao_axial,
                            altura=altura_casa,
                            tipo=tipo,
                            ancora=self)
                self.tiles[(q, r)] = tile

        self.mapa = [[self.tiles[(q, r)] for q, _ in enumerate(linha)] for r, linha in enumerate(self.mapa_base)]










