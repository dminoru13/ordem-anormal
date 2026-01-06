import pygame
from tabuleiro import criar_tabuleiro

pygame.init()

#VARIACEIS GLOBAIS

tamanho_tela = (940, 940)


#COISAS BASICAS PYGAME

tela = pygame.display.set_mode(tamanho_tela)
clock = pygame.time.Clock()

tabuleiro = criar_tabuleiro((100,100), 5, 5, (100, 100, 100))
tabuleiro2 = criar_tabuleiro((100,500), 15, 5, (200, 100, 100))







#O JOGO RODANDO

rodando = True
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    tela.fill((30, 30, 30))




    tela.blit(tabuleiro[0], tabuleiro[1])
    tela.blit(tabuleiro2[0], tabuleiro2[1])


    pygame.display.flip()
    clock.tick(60)

pygame.quit()