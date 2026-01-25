from symtable import Class

import pygame
from base.configuracao import config


class Came:
    def __init__(self):
        self.camera_x = 10
        self.camera_y = 10
        self.zoom = 1




    def criar_tela(self, tamanho = config.tamanho_tela, nome = "onirociencia"):
        pygame.display.set_caption(nome)
        tela = pygame.display.set_mode(tamanho)

        return tela

    def cordenadas_globais_mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        posicao_mundo_x = self.camera_x + mouse_x / config.tamanho_dos_tiles
        posicao_mundo_y = self.camera_y + mouse_y / config.tamanho_dos_tiles
        return posicao_mundo_x, posicao_mundo_y


    def evento(self, evento):

        if evento.type == pygame.MOUSEWHEEL:
            antes = self.cordenadas_globais_mouse()


            self.zoom *= 1.1 if evento.y > 0 else 0.9
            config.tamanho_dos_tiles = config.tamanho_base_tiles * self.zoom

            depois = self.cordenadas_globais_mouse()

            self.camera_x += antes[0] - depois[0]
            self.camera_y += antes[1] - depois[1]



            print(config.tamanho_dos_tiles)


        teclas = pygame.key.get_pressed()


        if teclas[pygame.K_w]:
            self.camera_y -= 10

        if teclas[pygame.K_s]:
            self.camera_y += 10

        if teclas[pygame.K_d]:
            self.camera_x -= 10

        if teclas[pygame.K_a]:
            self.camera_x += 10

Camera = Came()