import pygame

from base.transform import Transform
from base.entidade import Entidades
from base.configuracao import config
from base.camera import Camera
from debug.texto_debug import Chat

class Retangulo_debug(Transform, Entidades):
    def __init__(self, posicao, cor = (255, 0, 0), tamanho = (config.largura_hexagono/2, config.altura_hexagono/2)):
        super().__init__(posicao=posicao, altura=0, clicavel=True, tamanho=(config.largura_hexagono, config.altura_hexagono))
        self.escala_anterior = config.tamanho_dos_tiles

        self.cor = cor

        self.tamanho = tamanho






    def centralizar_camera(self):
        x,y = self.posicao_mundo_pixel

        Camera.focar_em((x + self.surface.get_size()[0]/2, y + self.surface.get_size()[1]/2))

    def evento(self, evento):

        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_w]:
            self.posicao_tile[1] -= 0.1

        if teclas[pygame.K_s]:
            self.posicao_tile[1] += 0.1

        if teclas[pygame.K_d]:
            self.posicao_tile[0] += 0.1

        if teclas[pygame.K_a]:
            self.posicao_tile[0] -= 0.1

        if teclas[pygame.K_SPACE]:
            print(self.cordenadas_globais_mouse())





    def desenhar(self, tela, transform: Transform | None = None):
        self.atualizar_escala()
        super().desenhar(tela, transform)

        self.centralizar_camera()






    def atualizar_escala(self):
        if self.escala_anterior == config.tamanho_dos_tiles:
            return

        self.surface = pygame.Surface((config.largura_hexagono, config.altura_hexagono), pygame.SRCALPHA)


    def foi_clicado(self, botao):
        pass


