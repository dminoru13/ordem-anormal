from variaveis_globais import *
from mundo.tabuleiro.tabuleiro import Tabuleiro
from mundo.pecas.pecas import Peca


#COISAS BASICAS PYGAME
pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()


#LISTAS

lista_pecas = [
        Peca("rodrigo", (7,7), 0)
    ]

lista_de_tabuleiros = [
    Tabuleiro((5,5), 0, 0, 5),
    Tabuleiro((5,5), 0, 2, 5),
]


#O JOGO RODANDO

rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        for pecas in lista_pecas:
            pecas.evento(event)

        for tabuleiros in lista_de_tabuleiros:
            tabuleiros.evento(event)




#DESENHNADO NA TELA

    tela.fill((30, 30, 30))

    for tabuleiro in lista_de_tabuleiros:
        tabuleiro.desenhar(tela)


    for peca in lista_pecas:
        peca.desenhar(tela)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()