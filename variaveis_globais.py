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


cor_borda = [
    (200, 180, 140),  # bege clássico – borda levemente mais escura
    (150, 0, 0),      # vermelho escuro queimado – borda mais intensa
    (180, 200, 170),  # verde pálido – borda sutil
    (50, 80, 60),     # verde musgo – borda mais escura
    (190, 190, 190),  # cinza claro – borda cinza médio
    (30, 30, 30),     # cinza carvão – borda preta quase total
    (210, 190, 150),  # pergaminho – borda levemente mais escura
    (90, 70, 40),     # marrom escuro – borda mais escura
    (170, 200, 230),  # azul gelo – borda suave e visível
    (10, 30, 60),     # azul marinho – borda bem escura
    (230, 230, 200),  # creme – borda levemente mais escura
    (50, 10, 10)      # vinho escuro – borda mais intensa
]
