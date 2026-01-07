import pygame
from tabuleiro.tabuleiro import criar_tabuleiro
from variaveis_globais import *


#COISAS BASICAS PYGAME
pygame.init()
tela = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()
#Tabuleiros

lista_de_tabuleiros = [
    criar_tabuleiro((6,1), 0, cor[1], cor[2])
]








#O JOGO RODANDO

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False



    tela.fill((30, 30, 30))




    for tabuleiro in lista_de_tabuleiros:
        tela.blit(*tabuleiro)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()