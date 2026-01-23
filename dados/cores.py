paleta = [
    # Combinação 0 – pergaminho (bege)
    (
        (155, 149, 125),
        (160, 159, 135),
        (175, 169, 145),
    ),

    # Combinação 1 – floresta (verde)
    (
        (180, 225, 185),  # verde claro
        (90, 160, 105),   # verde médio
        (40, 90, 55),     # verde escuro
    ),

    # Combinação 2 – pedra / ruínas (cinza)
    (
        (235, 235, 235),  # cinza claro
        (150, 150, 150),  # cinza médio
        (70, 70, 70),     # cinza escuro
    ),

    # Combinação 3 – gelo (azul)
    (
        (215, 230, 245),  # azul gelo claro
        (130, 170, 215),  # azul médio
        (50, 80, 130),    # azul escuro
    ),

    # Combinação 4 – pergaminho escuro (marrom)
    (
        (220, 200, 170),  # marrom claro
        (150, 115, 75),   # marrom médio
        (90, 60, 30),     # marrom escuro
    ),

    # Combinação 5 – creme (amarelado)
    (
        (250, 248, 225),  # creme claro
        (215, 205, 165),  # creme médio
        (170, 155, 110),  # creme escuro
    ),
]



#aaaaa
def gerar_cor_borda(cor):
    fator = 0.8
    minimo = 30

    r,g,b = cor
    r_b = int(r - (r - minimo)* fator)
    g_b = int(g - (g - minimo) * fator)
    b_b = int(b - (b - minimo) * fator)

    return (r_b, g_b, b_b)

def clareamento_por_altura(cor, altura):

    fator = (2 - altura)/5
    minimo = 0

    r, g, b = cor
    r_b = int(r - (r - minimo) * fator)
    g_b = int(g - (g - minimo) * fator)
    b_b = int(b - (b - minimo) * fator)

    return (r_b, g_b, b_b)