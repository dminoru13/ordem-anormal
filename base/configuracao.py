import math


class Configuracao:
    def __init__(self):
        self.tamanho_base_tiles = 64
        self.tamanho_dos_tiles = self.tamanho_base_tiles
        self.tamanho_tela = (740, 740)

    @property
    def raio_hexagono(self):
        return self.tamanho_dos_tiles/2

    @property
    def altura_hexagono(self):
        return self.tamanho_dos_tiles/2 * math.sqrt(3)

    @property
    def largura_hexagono(self):
        return self.tamanho_dos_tiles

debug = 0

config = Configuracao()