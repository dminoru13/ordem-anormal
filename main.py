import pygame
from dados.configuracao import tamanho_tela
from mundo.tabuleiro.tabuleiro import Tabuleiro
from mundo.pecas.pecas import Peca
import math




#COISAS BASICAS PYGAME
pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()


#LISTAS

lista_pecas = [
        Peca("rodrigo", (7,7), 0)
    ]

lista_de_tabuleiros = [
    Tabuleiro(posicao= (5,5), altura= 0, mapa_base= 0, cor_tile= 5),
]


#O JOGO RODANDO

rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        for pecas in lista_pecas:
            pecas.evento(event)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if peca.rect.collidepoint(event.pos):
                    peca.estou_no_tabuleiro(lista_de_tabuleiros[0])





#DESENHNADO NA TELA

    tela.fill((30, 30, 30))

    for tabuleiros in lista_de_tabuleiros:
        for linha in tabuleiros.mapa:
            for tile in linha:
                tile.desenhar(tela)

    for peca in lista_pecas:
        peca.desenhar(tela)



    pygame.display.flip()
    clock.tick(60)

pygame.quit()


