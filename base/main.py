import pygame

from base.configuracao import tamanho_tela
from mundo.tabuleiro.tabuleiro import Tabuleiro
from mundo.pecas.pecas import Peca
import camera
import configuracao

#COISAS BASICAS PYGAME
pygame.init()

tela = camera.criar_tela(tamanho_tela, "onirociencia")

clock = pygame.time.Clock()




#LISTAS



lista_de_tabuleiros = [
    Tabuleiro(posicao= (1,1), altura= 0, mapa_base= 0, cor_tile= 0),
]

lista_pecas = [
        Peca("rodrigo", (0,5), 0, lista_de_tabuleiros[0])
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




        for pecas in lista_pecas:
            pecas.evento(event)

        for tabuleiros in lista_de_tabuleiros:
            for linha in tabuleiros.mapa:
                for casa in linha:
                    casa.evento(event)

        if event.type == pygame.MOUSEWHEEL:
            configuracao.tamanho_dos_tiles += event.y
            print(configuracao.tamanho_dos_tiles)


    teclas = pygame.key.get_pressed()


    if teclas[pygame.K_w]:
        camera.camera_y += 1

    if teclas[pygame.K_s]:
        camera.camera_y -= 1

    if teclas[pygame.K_d]:
        camera.camera_x -= 1

    if teclas[pygame.K_a]:
        camera.camera_x += 1







#DESENHNADO NA TELA

    tela.fill((30, 30, 40))

    ordenanar_desenho()




    pygame.display.flip()


pygame.quit()



