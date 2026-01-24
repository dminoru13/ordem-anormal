paleta = [
    # Combinação 0 – pergaminho (bege)
    (
        (45, 39, 65),
        (50, 49, 65),
        (65, 59, 75),
    ),
]

cor_borda = (70, 45, 50)
cor_parede = (100, 100, 100)



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