from pecas.visual_peca import criar_pecas
from tabuleiro.visual_tabuleiro import criar_tabuleiro, cor

lista_pecas = [
        {
            "nome": "roberto",
            "surface": criar_pecas()[0],
            "rect": criar_pecas()[1],
            "posicao": (6,5)
         },

        {
            "nome": "mariao",
            "surface": criar_pecas()[0],
            "rect": criar_pecas()[1],
            "posicao": (8,3)
         },
        {
            "nome": "afweasaf",
            "surface": criar_pecas()[0],
            "rect": criar_pecas()[1],
            "posicao": (10,3)
         }
    ]

lista_de_tabuleiros = [
    criar_tabuleiro((6,1), 0, cor[1], cor[2])
]