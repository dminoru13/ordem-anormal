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
        Peca("rodrigo", (3,6), 0)
    ]

lista_de_tabuleiros = [
    Tabuleiro(posicao= (1,1), altura= 0, mapa_base= 0, cor_tile= 5),
]



def ordenanar_desenho():

   array_geral = []

   for tabuleiros in lista_de_tabuleiros:
       for linha in tabuleiros.mapa:
           array_geral.extend(linha)

   array_geral.extend(lista_pecas)

   array_geral.sort(key=lambda e: (e.posicao_mundo_pixel_sem_altura[1]))

   for item in array_geral: item.desenhar(tela)




#O JOGO RODANDO

rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False




        for pecas in lista_pecas:
            pecas.evento(event)

        for tabuleiros in lista_de_tabuleiros:
            for linha in tabuleiros.mapa:
                for casa in linha:
                    casa.evento(event)






#DESENHNADO NA TELA

    tela.fill((30, 30, 30))

    ordenanar_desenho()




    pygame.display.flip()
    clock.tick(60)

pygame.quit()



