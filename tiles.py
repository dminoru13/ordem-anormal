import pygame

tamanho_dos_tiles = 32

def criar_tiles(cor):
    quadrado = pygame.Surface((tamanho_dos_tiles, tamanho_dos_tiles*1.5), pygame.SRCALPHA)
    pygame.draw.rect(quadrado, cor, (0, 0, tamanho_dos_tiles, tamanho_dos_tiles))
    pygame.draw.rect(quadrado, (cor[0]/2, cor[1]/2, cor[2]/2), (0, tamanho_dos_tiles, tamanho_dos_tiles, tamanho_dos_tiles/2))
    return quadrado