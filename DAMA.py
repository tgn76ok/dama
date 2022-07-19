import pygame
from pygame.locals import *
import estilo.color

pygame.init()
# VARIÁVEIS DE VALOR CONSTANTE

LARGURA = 800
ALTURA = 600


# INICIANDO PROGRAMAÇÃO DO DISPLAY
tela = pygame.display.set_mode((830, 635))
pygame.display.set_caption('Jogo de Damas')
iniciodotabuleiro = [
    ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
    [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
    ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
    ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
    [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
]

matriz = iniciodotabuleiro[:]
jogadapossivel = []
jogadapossivel2 = []
colunaplayer1, linhaplayer1, colunaplayer2, linhaplayer2 = 0, 0, 0, 0
clickX = 1000
clicky = 1000
coluna = 0
linha = 0
turnos = True
jogadoratual = 0
pontos = 0
pontospossiveis2 = []
pontospossiveis1 = []
pedras = []
linhaorginBlack = 0
colunaorginBlack = 0

while True:

    precionado = bool()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            precionado = True
        if event.type == pygame.MOUSEBUTTONUP:
            precionado = False
            clickX = 1000
            clicky = 1000
        if precionado:
            mousex, mousey = pygame.mouse.get_pos()

            if 0 <= mousex < 75:
                coluna = 0
            if 75 <= mousex < 75 * 2:
                coluna = 1
            if 75 * 2 <= mousex < 75 * 3:
                coluna = 2
            if 75 * 3 <= mousex < 75 * 4:
                coluna = 3
            if 75 * 4 <= mousex < 75 * 5:
                coluna = 4
            if 75 * 5 <= mousex < 75 * 6:
                coluna = 5
            if 75 * 6 <= mousex < 75 * 7:
                coluna = 6
            if 75 * 7 <= mousex < 75 * 8:
                coluna = 7
            if 0 <= mousey < 75:
                linha = 0
            if 75 <= mousey < 75 * 2:
                linha = 1
            if 75 * 2 <= mousey < 75 * 3:
                linha = 2
            if 75 * 3 <= mousey < 75 * 4:
                linha = 3
            if 75 * 4 <= mousey < 75 * 5:
                linha = 4
            if 75 * 5 <= mousey < 75 * 6:
                linha = 5
            if 75 * 6 <= mousey < 75 * 7:
                linha = 6
            if 75 * 7 <= mousey < 75 * 8:
                linha = 7

            clickX, clicky = 75 * coluna, 75 * linha
    # desenhar tabuleiro
    matriz1 = []

    posiçoes = ['1', '2']
    for i in range(8):
        if i % 2 == 0:
            matriz1.append(posiçoes * 4)
        else:
            posiçoes.reverse()
            matriz1.append(posiçoes * 4)
            posiçoes.reverse()

    y1 = 0
    for l in range(len(matriz1)):
        x1 = 0
        for c in range(len(matriz1[l])):
            if matriz1[l][c] == '1':
                pygame.draw.rect(tela, estilo.color.COR_TABULEIRO, (x1, y1, 75, 75))
            else:
                pygame.draw.rect(tela, estilo.color.BRANCO, (x1, y1, 75, 75))

            x1 += 75
        y1 += 75
    # ---------------------------------------------------------------------------------------#
    # desenhar pedras com forme a matriz
    y = 0
    for l in range(len(matriz)):
        x = 0
        for c in range(len(matriz[l])):
            if matriz[l][c] == 'p':
                pygame.draw.circle(tela, estilo.color.PRETO, (x + 35, y + 35), 25, 25)
            elif matriz[l][c] == 'b':
                pygame.draw.circle(tela, estilo.color.AZUL, (x + 35, y + 35), 25, 25)

            x += 75
        y += 75

    if turnos:
        # turno das brancas
        if (linha + coluna) % 2 == 0:
            pygame.draw.rect(tela, estilo.color.verde_mais_claro, (clickX, clicky, 75, 75))
            for l in range(len(matriz)):
                for c in range(len(matriz[l])):
                    if matriz[l][c] != ' ' and matriz[l][c] != 'p':
                        if l * 75 == clicky and c * 75 == clickX:
                            #A CASA QEU o jagador um jogou
                            pygame.draw.circle(tela, estilo.color.VERMELHO, (clickX + 35, clicky + 35), 25, 25)
                            colunaplayer1, linhaplayer1 = c, l
                            print(linhaplayer1, colunaplayer1)


                    elif matriz[l][c] == ' ':
                        # if c ==0 or c ==7 or y ==0 or y ==7:

                        if matriz[linhaplayer1 - 1][colunaplayer1 - 1] == ' ':
                            jogadas = (colunaplayer1 - 1, linhaplayer1 - 1)
                            jogadapossivel.append(jogadas)
                            pygame.draw.rect(tela, estilo.color.AZUL,
                                             ((colunaplayer1 - 1) * 75, (linhaplayer1 - 1) * 75, 75, 75))
                        if colunaplayer1 != 7:
                            if matriz[linhaplayer1 - 1][colunaplayer1 + 1] == ' ':
                                jogadas = (colunaplayer1 + 1, linhaplayer1 - 1)
                                jogadapossivel.append(jogadas)
                                pygame.draw.rect(tela, estilo.color.AZUL,
                                                 ((colunaplayer1 + 1) * 75, (linhaplayer1 - 1) * 75, 75, 75))

                        for jogada in jogadapossivel:
                            if clickX == jogada[0] * 75 and clicky == jogada[1] * 75:
                                matriz[jogada[1]][jogada[0]] = 'b'
                                matriz[linhaplayer1][colunaplayer1] = ' '
                                turnos = False


                        jogadapossivel.clear()


                    # comer pedra petra

                    elif matriz[l][c] == 'p' or matriz[l][c] == ' ':
                        if matriz[linhaplayer1 - 1][colunaplayer1 - 1] == 'p':
                            # cima esquerda
                            if matriz[linhaplayer1 - 2][colunaplayer1 - 2] == ' ':

                                jogadadoplayer1 = (colunaplayer1 - 2, linhaplayer1 - 2)
                                pontospossiveis1.append(jogadadoplayer1)
                                pygame.draw.rect(tela, estilo.color.AZUL,
                                                 ((colunaplayer1 - 2) * 75, (linhaplayer1 - 2) * 75, 75, 75))

                                for pontos2 in pontospossiveis1:
                                    if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                        matriz[pontos2[1]][pontos2[0]] = 'b'
                                        matriz[linhaplayer1][colunaplayer1] = ' '
                                        matriz[linhaplayer1 - 1][colunaplayer1 - 1] = ' '
                                        turnos = False
                                        pontospossiveis1.clear()
                                        clicky, clickx = 0, 75

                        if colunaplayer1 != 7:
                            if matriz[linhaplayer1 - 1][colunaplayer1 + 1] == 'p':
                                if colunaplayer1 != 6:
                                    if matriz[linhaplayer1 - 2][colunaplayer1 + 2] == ' ':
                                        # cima direita
                                        jogadadoplayer1 = (colunaplayer1 + 2, linhaplayer1 - 2)

                                        pontospossiveis1.append(jogadadoplayer1)
                                        pygame.draw.rect(tela, estilo.color.AZUL,
                                                         ((colunaplayer1 + 2) * 75, (linhaplayer1 - 2) * 75, 75, 75))
                                        for pontos2 in pontospossiveis1:
                                            if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                                matriz[pontos2[1]][pontos2[0]] = 'b'
                                                matriz[linhaplayer1][colunaplayer1] = ' '
                                                matriz[linhaplayer1 - 1][colunaplayer1 + 1] = ' '

                                                turnos = False
                                                pontospossiveis1.clear()
                                                clicky, clickx = 0, 75

                        if colunaplayer1 != 7 and linhaplayer1 != 7:
                            if matriz[linhaplayer1 + 1][colunaplayer1 + 1] == 'p':
                                if matriz[linhaplayer1 + 2][colunaplayer1 + 2] == ' ':
                                    # baixo direita
                                    jogadadoplayer1 = (colunaplayer1 + 2, linhaplayer1 + 2)
                                    pontospossiveis1.append(jogadadoplayer1)
                                    pygame.draw.rect(tela, estilo.color.AZUL,
                                                     ((colunaplayer1 + 2) * 75, (linhaplayer1 + 2) * 75, 75, 75))

                                    for pontos2 in pontospossiveis1:
                                        if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                            matriz[pontos2[1]][pontos2[0]] = 'b'
                                            matriz[linhaplayer1][colunaplayer1] = ' '
                                            matriz[linhaplayer1 + 1][colunaplayer1 + 1] = ' '

                                            turnos = False
                                            clicky, clickx = 0, 75
                                            pontospossiveis1.clear()




                        if linhaplayer1 != 7:
                            if matriz[linhaplayer1 + 1][colunaplayer1 - 1] == 'p':
                                if matriz[linhaplayer1 + 2][colunaplayer1 - 2] == ' ':
                                    # baixo esquerda
                                    jogadadoplayer1 = (colunaplayer1 - 2, linhaplayer1 + 2)
                                    pontospossiveis1.append(jogadadoplayer1)
                                    pygame.draw.rect(tela, estilo.color.AZUL,
                                                     ((colunaplayer1 - 2) * 75, (linhaplayer1 + 2) * 75, 75, 75))

                                    for pontos2 in pontospossiveis1:
                                        if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                            matriz[pontos2[1]][pontos2[0]] = 'b'
                                            matriz[linhaplayer1][colunaplayer1] = ' '
                                            matriz[linhaplayer1 + 1][colunaplayer1 - 1] = ' '

                                            turnos = False
                                            pontospossiveis1.clear()
                                            clicky, clickx = 0, 75







    # TURNO DAS PRETAS

    else:
        if (linha + coluna) % 2 == 0:
            pygame.draw.rect(tela, estilo.color.verde_mais_claro, (clickX, clicky, 75, 75))
            for l in range(len(matriz)):
                for c in range(len(matriz[l])):
                    if matriz[l][c] != ' ' and matriz[l][c] != 'b':
                        if l * 75 == clicky and c * 75 == clickX:
                            pygame.draw.circle(tela, estilo.color.VERMELHO, (clickX + 35, clicky + 35), 25, 25)
                            linhaplayer2, colunaplayer2 = l, c

                    elif matriz[l][c] == ' ':
                        if colunaplayer2 != 7 and linhaplayer2 != 7:
                            if matriz[linhaplayer2 + 1][colunaplayer2 + 1] == ' ':
                                jogadas = (colunaplayer2 + 1, linhaplayer2 + 1)
                                jogadapossivel2.append(jogadas)
                                pygame.draw.rect(tela, estilo.color.AZUL,
                                                 ((colunaplayer2 + 1) * 75, (linhaplayer2 + 1) * 75, 75, 75))
                        if linhaplayer2 != 7:
                            if matriz[linhaplayer2 + 1][colunaplayer2 - 1] == ' ':
                                jogadas = (colunaplayer2 - 1, linhaplayer2 + 1)
                                jogadapossivel2.append(jogadas)
                                pygame.draw.rect(tela, estilo.color.AZUL,
                                                 ((colunaplayer2 - 1) * 75, (linhaplayer2 + 1) * 75, 75, 75))

                        for jogada in jogadapossivel2:
                            if clickX == jogada[0] * 75 and clicky == jogada[1] * 75:
                                matriz[jogada[1]][jogada[0]] = 'p'
                                matriz[linhaplayer2][colunaplayer2] = ' '

                                turnos = True
                                clicky, clickx = 0, 75
                                jogadapossivel2.clear()

                    # comer pedra

                    elif matriz[l][c] == 'b' or matriz[l][c] == ' ':

                        if matriz[linhaplayer2 - 1][colunaplayer2 - 1] == 'b':
                            # cima esquerda
                            if matriz[linhaplayer2 - 2][colunaplayer2 - 2] == ' ':

                                jogadadoplayer2 = (colunaplayer2 - 2, linhaplayer2 - 2)
                                pontospossiveis2.append(jogadadoplayer2)
                                pygame.draw.rect(tela, estilo.color.AZUL,
                                                 ((colunaplayer2 - 2) * 75, (linhaplayer2 - 2) * 75, 75, 75))

                                for pontos2 in pontospossiveis2:
                                    if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                        matriz[pontos2[1]][pontos2[0]] = 'p'
                                        matriz[linhaplayer2][colunaplayer2] = ' '
                                        matriz[linhaplayer2 - 1][colunaplayer2 - 1] = ' '
                                        turnos = True
                                        clicky, clickx = 0, 75
                                        pontospossiveis2.clear()



                        if colunaplayer2 != 7:
                            if matriz[linhaplayer2 - 1][colunaplayer2 + 1] == 'b':
                                if colunaplayer2 != 6:
                                    if matriz[linhaplayer2 - 2][colunaplayer2 + 2] == ' ':
                                        # cima baixo
                                        jogadadoplayer2 = (colunaplayer2 + 2, linhaplayer2 - 2)

                                        pontospossiveis2.append(jogadadoplayer2)
                                        pygame.draw.rect(tela, estilo.color.AZUL,
                                                         ((colunaplayer2 + 2) * 75, (linhaplayer2 - 2) * 75, 75, 75))

                                        for pontos2 in pontospossiveis2:
                                            if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                                matriz[pontos2[1]][pontos2[0]] = 'p'
                                                matriz[linhaplayer2][colunaplayer2] = ' '
                                                matriz[linhaplayer2 - 1][colunaplayer2 + 1] = ' '

                                                turnos = True
                                                clicky, clickx = 0, 75
                                                pontospossiveis2.clear()

                        if colunaplayer2 != 7 and linhaplayer2 != 7:
                            if matriz[linhaplayer2 + 1][colunaplayer2 + 1] == 'b':
                                if colunaplayer2 != 6 and linhaplayer2 != 7:
                                    if matriz[linhaplayer2 + 2][colunaplayer2 + 2] == ' ':
                                        # baixo direita
                                        jogadadoplayer2 = (colunaplayer2 + 2, linhaplayer2 + 2)

                                        pontospossiveis2.append(jogadadoplayer2)
                                        pygame.draw.rect(tela, estilo.color.AZUL,
                                                         ((colunaplayer2 + 2) * 75, (linhaplayer2 + 2) * 75, 75, 75))
                                        for pontos2 in pontospossiveis2:
                                            if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                                matriz[pontos2[1]][pontos2[0]] = 'p'
                                                matriz[linhaplayer2][colunaplayer2] = ' '
                                                matriz[linhaplayer2 + 1][colunaplayer2 + 1] = ' '

                                                turnos = True
                                                pontospossiveis2.clear()
                                                clicky, clickx = 0, 75

                        if linhaplayer2 != 7:
                            if matriz[linhaplayer2 + 1][colunaplayer2 - 1] == 'b':
                                if linhaplayer2 != 6:
                                    if matriz[linhaplayer2 + 2][colunaplayer2 - 2] == ' ':
                                        # baixo esquerda
                                        jogadadoplayer2 = (colunaplayer2 - 2, linhaplayer2 + 2)
                                        pontospossiveis2.append(jogadadoplayer2)
                                        pygame.draw.rect(tela, estilo.color.AZUL,
                                                         ((colunaplayer2 - 2) * 75, (linhaplayer2 + 2) * 75, 75, 75))

                                        for pontos2 in pontospossiveis2:
                                            if clickX == pontos2[0] * 75 and clicky == pontos2[1] * 75:
                                                matriz[pontos2[1]][pontos2[0]] = 'p'
                                                matriz[linhaplayer2][colunaplayer2] = ' '
                                                matriz[linhaplayer2 + 1][colunaplayer2 - 1] = ' '
                                                turnos = True
                                                clicky, clickx = 0, 75
                                                pontospossiveis2.clear()

    #    if 0 <= mousex<75:
    #        print('a')
    #    if 75 <= mousex < 75*2:
    #        print('b')
    #   if 75*2 <= mousex < 75*3:
    #        print('c')
    #    if 75*3 <= mousex < 75 * 4:
    #        print('d')
    #    if 75*4 <= mousex < 75*5:
    #        print('e')
    #    if 75*5 <= mousex < 75*6:
    #        print('f')
    #    if 75*6 <= mousex < 75*7:
    #        print('g')
    #    if 75 * 7 <= mousex < 75 * 8:
    #        print('h')
    #    if 0 <= mousey<75:
    #        print('8')
    #    if 75 <= mousey < 75*2:
    #        print('7')
    #    if 75*2 <= mousey < 75*3:
    #        print('6')
    #    if 75*3 <= mousey < 75 * 4:
    #        print('5')
    #    if 75*4 <= mousey < 75*5:
    #        print('4')
    #    if 75*5 <= mousey < 75*6:
    #        print('3')
    #    if 75*6 <= mousey < 75*7:
    #       print('2')
    #    if 75 * 7 <= mousey < 75 * 8:
    #        print('1')

    pygame.display.update()
