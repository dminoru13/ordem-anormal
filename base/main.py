import pygame

from mundo.tabuleiro.tabuleiro import Tabuleiro
from mundo.pecas.pecas import Peca
from camera import Camera
from debug.texto_debug import Chat
from debug.retangulo_debug import Retangulo_debug
from configuracao import config



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

lista_retangulos_debug = [
    Retangulo_debug((config.tamanho_tela[0]/2, config.tamanho_tela[1]/2))
]


def ordenanar_desenho():

   array_geral = []

   for tabuleiros in lista_de_tabuleiros:
       for linha in tabuleiros.mapa:
           array_geral.extend(linha)

   array_geral.extend(lista_pecas)

   array_geral.sort(key=lambda e: (e.posicao_mundo_pixel_sem_altura[1]))

   for item in array_geral: item.desenhar(tela)

   jose = lista_retangulos_debug[0]

   jose.desenhar(tela)



#O JOGO RODANDO

rodando = True
while rodando:

    dt = clock.tick(200)

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

    Chat.add_texto(texto= str(int(clock.get_fps())), id=0, tamanho= 30)
    Chat.add_texto(str(pygame.mouse.get_pos()), 1)
    Chat.add_texto(str((pygame.mouse.get_pos()[0] - Camera.camera_x, pygame.mouse.get_pos()[1] - Camera.camera_y)), 2)

    Chat.textar(tela)




    pygame.display.flip()


pygame.quit()



