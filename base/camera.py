from symtable import Class

import pygame
from base.configuracao import config
from UI.texto_debug import Chat


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
        posicao_mundo_x = self.camera_x + mouse_x
        posicao_mundo_y = self.camera_y + mouse_y
        return posicao_mundo_x, posicao_mundo_y


    def evento(self, evento):

        mouse_x, mouse_y = self.cordenadas_globais_mouse()

        Chat.add_texto("mouse_x: " + str(int(mouse_x)), 0)
        Chat.add_texto("mouse_y: " + str(int(mouse_y)), 1)

        if evento.type == pygame.MOUSEWHEEL:
            self.zoom *= 1.1 if evento.y > 0 else 0.9
            config.tamanho_dos_tiles = config.tamanho_base_tiles * self.zoom







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

        if teclas[pygame.K_SPACE]:
            print(self.cordenadas_globais_mouse())

Camera = Came()