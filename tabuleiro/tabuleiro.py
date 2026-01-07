from tabuleiro.visual_tabuleiro import criar_tabuleiro, cor
from pecas.pecas import peca

lista_pecas = [
        peca("rodrigo", (1,5)),
        peca("creusa", (3,3)),
        peca("jae", (5,1))
    ]

lista_de_tabuleiros = [
    criar_tabuleiro((6,1), 0, cor[1], cor[2])
]