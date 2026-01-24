import pygame
from dados.configuracao import tamanho_tela

camera_x = 10
camera_y = 10


def criar_tela(tamanho, nome):
    pygame.display.set_caption(nome)
    tela = pygame.display.set_mode(tamanho)

    return tela