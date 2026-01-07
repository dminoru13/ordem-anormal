import pygame
from variaveis_globais import *
from tabuleiro.tabuleiro import lista_pecas, lista_de_tabuleiros


#COISAS BASICAS PYGAME
pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()
#Tabuleiros


#O JOGO RODANDO

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for peca in lista_pecas:
                    if peca["rect"].collidepoint(event.pos):
                        print(peca["nome"])


#DESENHNADO NA TELA

    tela.fill((30, 30, 30))

    for tabuleiro in lista_de_tabuleiros:
        tela.blit(*tabuleiro)

    for peca in lista_pecas:
        pos_peca = tuple(valor*32 for valor in peca["posicao"])
        peca["rect"].topleft = pos_peca
        tela.blit(peca["surface"], peca["rect"])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()