import pygame
from dados.configuracao import debug
from base.transform import Transform

class TextoDebug:
    def __init__(self,tela,posicao,**kwargs):
        super().__init__(**kwargs)

        self.texto = ""
        self.tela = tela
        self.fonte = pygame.font.Font(None, 16)  # None = fonte padrão
        self.posicao = posicao

    def mudar_texto(self, texto):
        self.texto = texto

        self.texto_surface = self.fonte.render(
            self.texto,
            True,  # antialias (suavização)
            (255, 0, 0)  # cor do texto
        )

    def desenhar_texto(self):


        self.tela.blit(self.texto_surface, self.posicao)



