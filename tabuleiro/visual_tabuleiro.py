
def criar_tabuleiro(posicao, tipo, cor, cor2: tuple | None = None):

    posicao_tabuleiro = (posicao[0]*(tamanho_dos_tiles), posicao[1]*(tamanho_dos_tiles))

    mapa = mapas[tipo]

    tabuleiro_surface = pygame.Surface(
        (
             len(mapa[0])*(tamanho_dos_tiles),
            len(mapa)*(tamanho_dos_tiles) + tamanho_dos_tiles/2
        ),
        pygame.SRCALPHA
    )

    tiles1 = criar_tiles(cor)

    if cor2 is None:
        for Y, linha in enumerate(mapa):
            for X, tile in enumerate(linha):
                if tile[0] == 1:
                    tabuleiro_surface.blit(
                        tiles1,
                        ((tamanho_dos_tiles) * X,
                         (tamanho_dos_tiles ) * Y)
                    )

    if cor2 is not None:
        tiles2 = criar_tiles(cor2)

        for Y, linha in enumerate(mapa):
            for X, tile in enumerate(linha):
                if tile[0] == 1:
                    if Y % 2 == 1:
                        if X % 2 == 0:
                            tabuleiro_surface.blit(
                                tiles1,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )
                        else:
                            tabuleiro_surface.blit(
                                tiles2,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )
                    else:
                        if X % 2 == 0:
                            tabuleiro_surface.blit(
                                tiles2,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )
                        else:
                            tabuleiro_surface.blit(
                                tiles1,
                                ((tamanho_dos_tiles) * X,
                                 (tamanho_dos_tiles ) * Y)
                            )




    return  tabuleiro_surface, posicao_tabuleiro
