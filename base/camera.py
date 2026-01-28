import pygame
from base.configuracao import config




class Came:
    def __init__(self):
        self.offset_x = 0
        self.offset_y = 0
        self.zoom = 1

    # variaveis para controlar a camera com o mouse
        self.x_inicial = 0
        self.y_inicial = 0

    #CRIAR TELA

    def criar_tela(self, tamanho = config.tamanho_tela, nome = "onirociencia"):
        pygame.display.set_caption(nome)
        tela = pygame.display.set_mode(tamanho)

        return tela

    # ZOOM

    def evento(self, evento):

        mouse_pos = pygame.mouse.get_pos()

        if evento.type == pygame.MOUSEWHEEL:

            x_antes, y_antes = self.tela_para_mundo(mouse_pos)

            self.zoom *= 1.1 if evento.y > 0 else 0.9
            config.tamanho_dos_tiles = config.tamanho_base_tiles * self.zoom

            x_depois, y_depois = self.tela_para_mundo(mouse_pos)

            self.offset_x += (x_antes - x_depois)
            self.offset_y += (y_antes - y_depois)



            print(config.tamanho_dos_tiles)

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:
                self.x_inicial, self.y_inicial = pygame.mouse.get_pos()





    def rodando(self):
        botao_mouse = pygame.mouse.get_pressed()

        if botao_mouse[0]:
            self.offset_x -= (pygame.mouse.get_pos()[0] - self.x_inicial)
            self.offset_y -= (pygame.mouse.get_pos()[1] - self.y_inicial)

            self.x_inicial, self.y_inicial = pygame.mouse.get_pos()


    def focar_em(self, posicao):

        pass

    # CONVERSÃO

    def mundo_para_tela(self, posicao):
        tx = (posicao[0] - self.offset_x) * self.zoom
        ty = (posicao[1] - self.offset_y) * self.zoom

        return tx, ty

    def tela_para_mundo(self, posicao):
        mx = posicao[0] / self.zoom + self.offset_x
        my = posicao[1] / self.zoom + self.offset_y

        return mx, my




Camera = Came()