import pygame.font


class Texto_debug:
    def __init__(self):
        self.lista_textos = []

        self.fontes = [
            "arial",
            "verdana",
            "comic",
            "times"
        ]

    def add_texto(self, texto, id = None, fonte = 0, tamanho = 30, cor = (255, 255, 255)):
        if id == None:
            self.lista_textos.append([str(texto), len(self.lista_textos), pygame.font.SysFont(self.fontes[fonte], tamanho), cor, tamanho])


        elif id >= len(self.lista_textos):
            self.lista_textos.append([str(texto), id, pygame.font.SysFont(self.fontes[fonte], tamanho), cor, tamanho])

        else:
            self.lista_textos[id] = [str(texto), id, pygame.font.SysFont(self.fontes[fonte], tamanho), cor, tamanho]


    def textar(self, tela):
        for texto in self.lista_textos:
            tela.blit(texto[2].render(texto[0], True, texto[3]), (0,texto[4]*texto[1]))



Chat = Texto_debug()