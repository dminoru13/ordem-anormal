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

ordem_de_desenho = [
    
]

def ordenanar_desenho():

    array_geral = []
    array_provisoria = []


    #FUNÇÕES

    def checar_maior_altura():
        maior_altura = -math.inf

        for item in array_geral:

            if item.altura > maior_altura:
                maior_altura = item.altura

        return maior_altura

    def ordenar_provisorio():
        array_provisoria.sort(key=lambda e: e.posicao[1])

        for itens in array_provisoria:
            ordem_de_desenho.append(itens)

        array_provisoria.clear()


    #COLOCA GERAL NA ARRAY GERAL

    for tabuleiros in lista_de_tabuleiros:
        for linha in tabuleiros.mapa:
            for tile in linha:
                array_geral.append(tile)

    for peca in lista_pecas:
        array_geral.append(peca)



    def loop_principal():

        #PASSA OS MAIS ALTOS DO GERAL PRA ARRAY PROVISORIA

        if not array_provisoria:

            for item in array_geral:
                if item.altura == checar_maior_altura():
                    array_provisoria.append(item)
                    array_geral.remove(item)

        ordenar_provisorio()

        if array_geral:
            ordenanar_desenho()
            print(len(array_geral))
        if not array_geral:
            for item in ordem_de_desenho:
                item.desenhar()
                print(len(array_geral))






#O JOGO RODANDO

rodando = True
while rodando:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

        for pecas in lista_pecas:
            pecas.evento(event)



        if event.type == pygame.MOUSEBUTTONDOWN:
           print(lista_de_tabuleiros[0].mapa[0][0].vizinho("baixo"))

    ordenanar_desenho()



#DESENHNADO NA TELA

    tela.fill((30, 30, 30))





    pygame.display.flip()
    clock.tick(60)

pygame.quit()



