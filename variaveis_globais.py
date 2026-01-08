import pygame

tamanho_tela = (740, 740)
tamanho_dos_tiles = 32


cor = [
    # 0 – claro
    (240, 217, 181),  # bege clássico

    # 1 – escuro
    (100, 10, 0),  # vermelho escuro queimado

    # 2 – claro
    (225, 235, 220),  # verde pálido

    # 3 – escuro
    (70, 102, 85),  # verde musgo

    # 4 – claro
    (230, 230, 230),  # cinza claro

    # 5 – escuro
    (60, 60, 60),  # cinza carvão

    # 6 – claro
    (235, 222, 189),  # pergaminho

    # 7 – escuro
    (120, 90, 50),  # marrom escuro

    # 8 – claro
    (210, 225, 240),  # azul gelo

    # 9 – escuro
    (30, 45, 80),  # azul marinho

    # 10 – claro
    (245, 245, 220),  # creme

    # 11 – escuro
    (80, 20, 20),  # vinho escuro
]


def gerar_cor_borda(cor):
    fator = 0.8
    minimo = 30

    r,g,b = cor
    r_b = int(r - (r - minimo)* fator)
    g_b = int(g - (g - minimo) * fator)
    b_b = int(b - (b - minimo) * fator)

    return (r_b, g_b, b_b)