import pygame
from base.configuracao import debug


class TextoDebug:
    def __init__(self,tela,posicao,**kwargs):
        super().__init__(**kwargs)

        self.texto = ""
        self.tela = tela
        self.fonte = pygame.font.Font(None, 20)  # None = fonte padrão
        self.posicao = posicao

        self.texto_surface = self.fonte.render(
            self.texto,
            True,  # antialias (suavização)
            (255, 0, 0)  # cor do texto
        )

    def mudar_texto(self, texto):
        self.texto = str(texto)

        self.texto_surface = self.fonte.render(
            self.texto,
            True,  # antialias (suavização)
            (255, 0, 0)  # cor do texto
        )


    def desenhar_texto(self):
        if debug == 1:
            self.tela.blit(self.texto_surface, self.posicao)



