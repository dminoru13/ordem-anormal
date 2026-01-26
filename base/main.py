import pygame

from mundo.tabuleiro.tabuleiro import Tabuleiro
from mundo.pecas.pecas import Peca
from camera import Camera
from UI.texto_debug import Chat



#COISAS BASICAS PYGAME
pygame.init()

tela = Camera.criar_tela(nome="onirociencia")

clock = pygame.time.Clock()

#LISTAS



lista_de_tabuleiros = [
    Tabuleiro(posicao= (0,0), altura= 0, mapa_base= 0, cor_tile= 0),
]

lista_pecas = [
        Peca("rodrigo", (5,0), 0, lista_de_tabuleiros[0])
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

    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False


        Camera.evento(event)

        for pecas in lista_pecas:
            pecas.evento(event)

        for tabuleiros in lista_de_tabuleiros:
            for linha in tabuleiros.mapa:
                for casa in linha:
                    casa.evento(event)









#DESENHNADO NA TELA

    tela.fill((30, 30, 40))

    ordenanar_desenho()

    Chat.textar(tela)




    pygame.display.flip()


pygame.quit()



