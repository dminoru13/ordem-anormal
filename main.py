from variaveis_globais import *
from tabuleiro.tabuleiro import lista_pecas, lista_de_tabuleiros
from pecas.pecas import peca


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
                    if peca.foi_clicado(event.pos, 1):
                        print(peca.nome)


#DESENHNADO NA TELA

    tela.fill((30, 30, 30))

    for tabuleiro in lista_de_tabuleiros:
        tela.blit(*tabuleiro)

    for peca in lista_pecas:
        peca.desenhar(tela)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()