

class Dama:
    def __init__(self):
        self.matriz = [
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 0
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 1
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 2
            [' ', ' ', ' ', ' ', 'B', ' ', ' ', ' '],  # 3
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 4
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 5
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 6
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 7
            # 0    1    2    3    4    5    6    7
        ]
        self.truno = 0

        pass

    # funçoes de status do tabuleiro

    def pedras_brancas_comuns_possiveis_de_mover_sem_comer(self):
        matriz = self.matriz

        posicoes_possiveis_das_brancas_sem_comer = {}

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'b':  # posiçao de todas as brancas

                    if coluna != 7 and linha != 0:
                        if matriz[linha-1][coluna+1] == ' ':

                            conjunto_de_pedras_posivel_jogada = linha, coluna

                            casas_origin = str(
                                conjunto_de_pedras_posivel_jogada)

                            casas_jogaveis = linha-1, coluna+1

                            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                    casas_jogaveis]
                            else:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                    casas_jogaveis]

                    if coluna != 0 and linha != 0:
                        if matriz[linha-1][coluna-1] == ' ':

                            conjunto_de_pedras_posivel_jogada = linha, coluna

                            casas_origin = str(
                                conjunto_de_pedras_posivel_jogada)

                            casas_jogaveis = linha-1, coluna+1

                            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                    casas_jogaveis]
                            else:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                    casas_jogaveis]

        return posicoes_possiveis_das_brancas_sem_comer

    def pedras_brancas_damas_possiveis_de_mover_sem_comer(self):
        matriz = self.matriz
        posicoes_possiveis_das_brancas_sem_comer = {}

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'B':
                    vare_cima_direita_linha = vare_cima_esquerda_linha = vare_baixo_esquerda_linha = vare_baixo_direita_linha = linha
                    vare_cima_direita_coluna = vare_cima_esquerda_coluna = vare_baixo_esquerda_coluna = vare_baixo_direita_coluna = coluna

                    conjunto_de_pedras_posivel_jogada = linha, coluna

                    if ((vare_cima_direita_linha > 0) and (vare_cima_direita_coluna < 7)):  # subir para direita
                        # subir para direita
                        # subir para direita
                        while matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == 'B' or matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':

                            # subir para direita
                            if matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)

                                casas_jogaveis = vare_cima_direita_linha, vare_cima_direita_coluna

                                if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_cima_direita_linha > 0 and vare_cima_direita_linha < 7) and (vare_cima_direita_coluna > 0 and vare_cima_direita_coluna < 7)):
                                    break

                            vare_cima_direita_linha -= 1
                            vare_cima_direita_coluna += 1

                    if vare_cima_esquerda_linha > 0 and vare_cima_esquerda_coluna > 0:  # subir para esqurda
                        # subir para esqurda
                        while matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == 'B' or matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':

                            # subir para esqurda
                            if matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)
                                casas_jogaveis = vare_cima_esquerda_linha, vare_cima_esquerda_coluna

                                if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_cima_esquerda_linha > 0 and vare_cima_esquerda_linha < 7) and (vare_cima_esquerda_coluna > 0 and vare_cima_esquerda_coluna < 7)):
                                    break

                            vare_cima_esquerda_linha -= 1
                            vare_cima_esquerda_coluna -= 1

                    if vare_baixo_esquerda_linha < 7 and vare_baixo_esquerda_coluna > 0:  # baixo para esqurda
                        # baixo para esqurda
                        while matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == 'B' or matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':

                            # baixo para esqurda
                            if matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':

                                conjunto_de_pedras_posivel_jogada = linha, coluna

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)

                                casas_jogaveis = vare_baixo_esquerda_linha, vare_baixo_esquerda_coluna

                                if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_baixo_esquerda_linha > 0 and vare_baixo_esquerda_linha < 7) and (vare_baixo_esquerda_coluna > 0 and vare_baixo_esquerda_coluna < 7)):
                                    break

                            vare_baixo_esquerda_linha += 1
                            vare_baixo_esquerda_coluna -= 1

                    if vare_baixo_direita_linha < 7 and vare_baixo_direita_coluna < 7:  # baixo para direita
                        # baixo para direita
                        while matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == 'B' or matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':

                            # baixo para direita
                            if matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':

                                conjunto_de_pedras_posivel_jogada = linha, coluna

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)

                                casas_jogaveis = vare_baixo_direita_linha, vare_baixo_direita_coluna

                                if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_baixo_direita_linha > 0 and vare_baixo_direita_linha < 7) and (vare_baixo_direita_coluna > 0 and vare_baixo_direita_coluna < 7)):
                                    break

                            vare_baixo_direita_linha += 1
                            vare_baixo_direita_coluna += 1

        return posicoes_possiveis_das_brancas_sem_comer

    def pedras_brancas_comuns_possiveis_de_comer(self):
        matriz = self.matriz
        pedras_brancas_possiveis_de_comer = dict()

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'b':  # posiçao de todas as brancas

                    if coluna < 7 and linha > 0:  # subir direita
                        if matriz[linha-1][coluna+1] in 'pP':
                            if coluna < 6 and linha > 1:
                                if matriz[linha-2][coluna+2] == ' ':

                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha-2, coluna+2

                                    if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_brancas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_brancas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]

                    if coluna > 0 and linha > 0:
                        if matriz[linha-1][coluna-1] in 'pP':
                            if coluna > 1 and linha > 1:
                                if matriz[linha-2][coluna-2] == ' ':

                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha-2, coluna-2

                                    if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_brancas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_brancas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]
                    if coluna < 7 and linha < 7:

                        if matriz[linha+1][coluna+1] in 'pP':

                            if coluna < 6 and linha < 6:
                                if matriz[linha+2][coluna+2] == ' ':

                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha+2, coluna+2

                                    if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_brancas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_brancas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]

                    if coluna > 0 and linha < 7:
                        if matriz[linha+1][coluna-1] in 'pP':
                            if coluna > 1 and linha < 6:
                                if matriz[linha+2][coluna-2] == ' ':

                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha+2, coluna-2

                                    if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_brancas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_brancas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]

        return pedras_brancas_possiveis_de_comer

    def pedras_brancas_dama_possiveis_de_comer(self):
        matriz = self.matriz
        posissoes_pedras_pretas_para_brancas_comer = dict()

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'B':  # dama
                    linha1 = linha2 = linha3 = linha4 = linha
                    coluna1 = coluna2 = coluna3 = coluna4 = coluna

                    while True:  # subir para direita
                        if not ((linha1 > 0 and linha1 < 7) and (coluna1 > 0 and coluna1 < 7)):
                            break
                        if matriz[linha1][coluna1] in 'Pp':  # subir para direita

                            ProLinha, ProColuna = linha1-1, coluna1+1

                            if matriz[ProLinha][ProColuna] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna
                                casas_origin = str(
                                    conjunto_de_pedras_posivel_de_comer)

                                casa_oponete = linha1, coluna1, -1

                                if posissoes_pedras_pretas_para_brancas_comer.get(casas_origin) is None:
                                    posissoes_pedras_pretas_para_brancas_comer[casas_origin] = [
                                        casa_oponete]

                                while (not (matriz[ProLinha][ProColuna] != ' ')):

                                    casas_jogaveis = ProLinha, ProColuna

                                    posissoes_pedras_pretas_para_brancas_comer[casas_origin] += [
                                        casas_jogaveis]

                                    if (ProColuna >= 7 and ProLinha == 0):
                                        break
                                    ProLinha -= 1
                                    ProColuna += 1

                        linha1 -= 1
                        coluna1 += 1
                    while True:  # subir para esquerda
                        if not ((linha2 > 0 and linha2 < 7) and (coluna2 > 0 and coluna2 < 7)):
                            break
                        if matriz[linha2][coluna2] in 'pP':  # subir para esquerda
                            if matriz[linha2-1][coluna2-1] == ' ':
                                ProLinha, ProColuna = linha2-1, coluna2-1

                                if matriz[ProLinha][ProColuna] == ' ':
                                    conjunto_de_pedras_posivel_de_comer = linha, coluna
                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casa_oponete = linha2, coluna2, -1

                                    if posissoes_pedras_pretas_para_brancas_comer.get(casas_origin) is None:
                                        posissoes_pedras_pretas_para_brancas_comer[casas_origin] = [
                                            casa_oponete]

                                    while (not (matriz[ProLinha][ProColuna] != ' ')):

                                        casas_jogaveis = ProLinha, ProColuna

                                        posissoes_pedras_pretas_para_brancas_comer[casas_origin] += [
                                            casas_jogaveis]

                                        if (ProColuna == 0 or ProLinha == 0):
                                            break
                                        ProLinha -= 1
                                        ProColuna -= 1

                        linha2 -= 1
                        coluna2 -= 1
                    while True:  # decer para esquerda

                        if not ((linha3 > 0 and linha3 < 7) and (coluna3 > 0 and coluna3 < 7)):
                            break
                        if matriz[linha3][coluna3] in 'Pp':  # subir para direita

                            ProLinha, ProColuna = linha3+1, coluna3-1

                            if matriz[ProLinha][ProColuna] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna
                                casas_origin = str(
                                    conjunto_de_pedras_posivel_de_comer)

                                casa_oponete = linha3, coluna3, -1

                                if posissoes_pedras_pretas_para_brancas_comer.get(casas_origin) is None:
                                    posissoes_pedras_pretas_para_brancas_comer[casas_origin] = [
                                        casa_oponete]

                                while (not (matriz[ProLinha][ProColuna] != ' ')):

                                    casas_jogaveis = ProLinha, ProColuna

                                    posissoes_pedras_pretas_para_brancas_comer[casas_origin] += [
                                        casas_jogaveis]

                                    if (ProLinha >= 7):
                                        break
                                    ProLinha += 1
                                    ProColuna -= 1

                        linha3 += 1
                        coluna3 -= 1
                    while True:  # decer para direita
                        if not ((linha4 >= 0 and linha4 < 7) and (coluna4 >= 0 and coluna4 < 7)):
                            break
                        if matriz[linha4][coluna4] in 'Pp':  # subir para direita

                            ProLinha, ProColuna = linha4+1, coluna4+1

                            if matriz[ProLinha][ProColuna] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna
                                casas_origin = str(
                                    conjunto_de_pedras_posivel_de_comer)

                                casa_oponete = linha4, coluna4, -1

                                if posissoes_pedras_pretas_para_brancas_comer.get(casas_origin) is None:
                                    posissoes_pedras_pretas_para_brancas_comer[casas_origin] = [
                                        casa_oponete]

                                while (not (matriz[ProLinha][ProColuna] != ' ')):

                                    casas_jogaveis = ProLinha, ProColuna

                                    posissoes_pedras_pretas_para_brancas_comer[casas_origin] += [
                                        casas_jogaveis]

                                    if (ProColuna >= 7 or ProLinha >= 7):
                                        break
                                    ProLinha += 1
                                    ProColuna += 1

                        linha4 += 1
                        coluna4 += 1

        return posissoes_pedras_pretas_para_brancas_comer

    def pedras_pretas_possiveis_de_mover_sem_comer(self):
        matriz = self.matriz

        posicoes_possiveis_das_pretas_sem_comer = {}

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'p':  # posiçao de todas as pretas

                    if coluna != 0 and linha != 7:
                        if matriz[linha+1][coluna-1] == ' ':

                            conjunto_de_pedras_posivel_jogada = linha, coluna

                            casas_origin = str(
                                conjunto_de_pedras_posivel_jogada)

                            casas_jogaveis = linha-1, coluna+1

                            if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [
                                    casas_jogaveis]
                            else:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] += [
                                    casas_jogaveis]

                    if coluna != 7 and linha != 7:

                        if matriz[linha+1][coluna+1] == ' ':

                            conjunto_de_pedras_posivel_jogada = linha, coluna

                            casas_origin = str(
                                conjunto_de_pedras_posivel_jogada)

                            casas_jogaveis = linha+1, coluna+1

                            if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [
                                    casas_jogaveis]
                            else:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] += [
                                    casas_jogaveis]

                elif matriz[linha][coluna] == 'P':

                    vare_cima_direita_linha = vare_cima_esquerda_linha = vare_baixo_esquerda_linha = vare_baixo_direita_linha = linha
                    vare_cima_direita_coluna = vare_cima_esquerda_coluna = vare_baixo_esquerda_coluna = vare_baixo_direita_coluna = coluna

                    conjunto_de_pedras_posivel_jogada = linha, coluna

                    if ((vare_cima_direita_linha > 0) and (vare_cima_direita_coluna < 7)):  # subir para direita
                        # subir para direita
                        # subir para direita
                        while matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == 'P' or matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':

                            # subir para direita
                            if matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)

                                casas_jogaveis = vare_cima_direita_linha, vare_cima_direita_coluna

                                if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_cima_direita_linha > 0 and vare_cima_direita_linha < 7) and (vare_cima_direita_coluna > 0 and vare_cima_direita_coluna < 7)):
                                    break

                            vare_cima_direita_linha -= 1
                            vare_cima_direita_coluna += 1

                    if vare_cima_esquerda_linha > 0 and vare_cima_esquerda_coluna > 0:  # subir para esqurda
                        # subir para esqurda
                        while matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == 'P' or matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':

                            # subir para esqurda
                            if matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)
                                casas_jogaveis = vare_cima_esquerda_linha, vare_cima_esquerda_coluna

                                if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_cima_esquerda_linha > 0 and vare_cima_esquerda_linha < 7) and (vare_cima_esquerda_coluna > 0 and vare_cima_esquerda_coluna < 7)):
                                    break

                            vare_cima_esquerda_linha -= 1
                            vare_cima_esquerda_coluna -= 1

                    if vare_baixo_esquerda_linha < 7 and vare_baixo_esquerda_coluna > 0:  # baixo para esqurda
                        # baixo para esqurda
                        while matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == 'P' or matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':

                            # baixo para esqurda
                            if matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':

                                conjunto_de_pedras_posivel_jogada = linha, coluna

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)

                                casas_jogaveis = vare_baixo_esquerda_linha, vare_baixo_esquerda_coluna

                                if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_baixo_esquerda_linha > 0 and vare_baixo_esquerda_linha < 7) and (vare_baixo_esquerda_coluna > 0 and vare_baixo_esquerda_coluna < 7)):
                                    break

                            vare_baixo_esquerda_linha += 1
                            vare_baixo_esquerda_coluna -= 1

                    if vare_baixo_direita_linha < 7 and vare_baixo_direita_coluna < 7:  # baixo para direita
                        # baixo para direita
                        while matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == 'P' or matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':

                            # baixo para direita
                            if matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':

                                conjunto_de_pedras_posivel_jogada = linha, coluna

                                casas_origin = str(
                                    conjunto_de_pedras_posivel_jogada)

                                casas_jogaveis = vare_baixo_direita_linha, vare_baixo_direita_coluna

                                if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [
                                        casas_jogaveis]
                                else:
                                    posicoes_possiveis_das_pretas_sem_comer[casas_origin] += [
                                        casas_jogaveis]

                                if not ((vare_baixo_direita_linha > 0 and vare_baixo_direita_linha < 7) and (vare_baixo_direita_coluna > 0 and vare_baixo_direita_coluna < 7)):
                                    break

                            vare_baixo_direita_linha += 1
                            vare_baixo_direita_coluna += 1

        return posicoes_possiveis_das_pretas_sem_comer

    def pedras_pretas_comuns_possiveis_de_comer(self):
        matriz = self.matriz
        pedras_pretas_possiveis_de_comer = dict()

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'p':  # posiçao de todas as brancas

                    if coluna < 7 and linha > 0:  # subir direita
                        if matriz[linha-1][coluna+1] in 'Bb':
                            if coluna < 6 and linha > 1:
                                if matriz[linha-2][coluna+2] == ' ':
                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha-2, coluna+2

                                    if pedras_pretas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_pretas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_pretas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]

                    if coluna > 0 and linha > 0:
                        if matriz[linha-1][coluna-1] in 'bB':
                            if coluna > 1 and linha > 1:
                                if matriz[linha-2][coluna-2] == ' ':
                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha-2, coluna-2

                                    if pedras_pretas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_pretas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_pretas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]
                    if coluna < 7 and linha < 7:

                        if matriz[linha+1][coluna+1] in 'bB':

                            if coluna < 6 and linha < 6:
                                if matriz[linha+2][coluna+2] == ' ':
                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha+2, coluna+2

                                    if pedras_pretas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_pretas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_pretas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]

                    if coluna > 0 and linha < 7:
                        if matriz[linha+1][coluna-1] in 'bB':
                            if coluna > 1 and linha < 6:
                                if matriz[linha+2][coluna-2] == ' ':

                                    conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casas_jogaveis = linha+2, coluna-2

                                    if pedras_pretas_possiveis_de_comer.get(casas_origin) is None:
                                        pedras_pretas_possiveis_de_comer[casas_origin] = [
                                            casas_jogaveis]
                                    else:
                                        pedras_pretas_possiveis_de_comer[casas_origin] += [
                                            casas_jogaveis]

        return pedras_pretas_possiveis_de_comer

    def pedras_pretas_dama_possiveis_de_comer(self):
        matriz = self.matriz
        posissoes_pedras_brancas_para_pretas_comer = dict()

        for linha in range(len(matriz)):
            for coluna in range(len(matriz)):
                if matriz[linha][coluna] == 'P':  # dama
                    linha1 = linha2 = linha3 = linha4 = linha
                    coluna1 = coluna2 = coluna3 = coluna4 = coluna

                    while True:  # subir para direita
                        if not ((linha1 > 0 and linha1 < 7) and (coluna1 > 0 and coluna1 < 7)):
                            break
                        if matriz[linha1][coluna1] in 'Bb':  # subir para direita

                            ProLinha, ProColuna = linha1-1, coluna1+1

                            if matriz[ProLinha][ProColuna] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna
                                casas_origin = str(
                                    conjunto_de_pedras_posivel_de_comer)

                                casa_oponete = linha1, coluna1, -1

                                if posissoes_pedras_brancas_para_pretas_comer.get(casas_origin) is None:
                                    posissoes_pedras_brancas_para_pretas_comer[casas_origin] = [
                                        casa_oponete]

                                while (not (matriz[ProLinha][ProColuna] != ' ')):

                                    casas_jogaveis = ProLinha, ProColuna

                                    posissoes_pedras_brancas_para_pretas_comer[casas_origin] += [
                                        casas_jogaveis]

                                    if (ProColuna >= 7 and ProLinha == 0):
                                        break
                                    ProLinha -= 1
                                    ProColuna += 1

                        linha1 -= 1
                        coluna1 += 1
                    while True:  # subir para esquerda
                        if not ((linha2 > 0 and linha2 < 7) and (coluna2 > 0 and coluna2 < 7)):
                            break
                        if matriz[linha2][coluna2] in 'Bb':  # subir para esquerda
                            if matriz[linha2-1][coluna2-1] == ' ':
                                ProLinha, ProColuna = linha2-1, coluna2-1

                                if matriz[ProLinha][ProColuna] == ' ':
                                    conjunto_de_pedras_posivel_de_comer = linha, coluna
                                    casas_origin = str(
                                        conjunto_de_pedras_posivel_de_comer)

                                    casa_oponete = linha2, coluna2, -1

                                    if posissoes_pedras_brancas_para_pretas_comer.get(casas_origin) is None:
                                        posissoes_pedras_brancas_para_pretas_comer[casas_origin] = [
                                            casa_oponete]

                                    while (not (matriz[ProLinha][ProColuna] != ' ')):

                                        casas_jogaveis = ProLinha, ProColuna

                                        posissoes_pedras_brancas_para_pretas_comer[casas_origin] += [
                                            casas_jogaveis]

                                        if (ProColuna == 0 or ProLinha == 0):
                                            break
                                        ProLinha -= 1
                                        ProColuna -= 1

                        linha2 -= 1
                        coluna2 -= 1
                    while True:  # decer para esquerda

                        if not ((linha3 > 0 and linha3 < 7) and (coluna3 > 0 and coluna3 < 7)):
                            break
                        if matriz[linha3][coluna3] in 'Bb':  # subir para direita

                            ProLinha, ProColuna = linha3+1, coluna3-1

                            if matriz[ProLinha][ProColuna] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna
                                casas_origin = str(
                                    conjunto_de_pedras_posivel_de_comer)

                                casa_oponete = linha3, coluna3, -1

                                if posissoes_pedras_brancas_para_pretas_comer.get(casas_origin) is None:
                                    posissoes_pedras_brancas_para_pretas_comer[casas_origin] = [
                                        casa_oponete]

                                while (not (matriz[ProLinha][ProColuna] != ' ')):

                                    casas_jogaveis = ProLinha, ProColuna

                                    posissoes_pedras_brancas_para_pretas_comer[casas_origin] += [
                                        casas_jogaveis]

                                    if (ProLinha >= 7):
                                        break
                                    ProLinha += 1
                                    ProColuna -= 1

                        linha3 += 1
                        coluna3 -= 1
                    while True:  # decer para direita
                        if not ((linha4 >= 0 and linha4 < 7) and (coluna4 >= 0 and coluna4 < 7)):
                            break
                        if matriz[linha4][coluna4] in 'Bb':  # subir para direita

                            ProLinha, ProColuna = linha4+1, coluna4+1

                            if matriz[ProLinha][ProColuna] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna
                                casas_origin = str(
                                    conjunto_de_pedras_posivel_de_comer)

                                casa_oponete = linha4, coluna4, -1

                                if posissoes_pedras_brancas_para_pretas_comer.get(casas_origin) is None:
                                    posissoes_pedras_brancas_para_pretas_comer[casas_origin] = [
                                        casa_oponete]

                                while (not (matriz[ProLinha][ProColuna] != ' ')):

                                    casas_jogaveis = ProLinha, ProColuna

                                    posissoes_pedras_brancas_para_pretas_comer[casas_origin] += [
                                        casas_jogaveis]

                                    if (ProColuna >= 7 or ProLinha >= 7):
                                        break
                                    ProLinha += 1
                                    ProColuna += 1

                        linha4 += 1
                        coluna4 += 1

        return posissoes_pedras_brancas_para_pretas_comer

    def Prioridade_caminhos_de_comer_pedras_comuns(self, PosiçaoDaPedra: str, num=0, oponete='Pp', caminho=[]):
        matriz = self.matriz
        cont = num

        print(caminho)
        if (PosiçaoDaPedra[1] == '-' or PosiçaoDaPedra[4] == '-'):
            return cont

        LinhaOrigin, ColunaOrigin = int(
            PosiçaoDaPedra[1]), int(PosiçaoDaPedra[4])
        if LinhaOrigin > 0 and ColunaOrigin < 7:  # subir direita
            if matriz[LinhaOrigin-1][ColunaOrigin+1] in oponete:

                if ColunaOrigin < 6 and LinhaOrigin > 1:

                    if matriz[LinhaOrigin-2][ColunaOrigin+2] == ' ':

                        if (self.tem_caminhos_de_comer(PosiçaoDaPedra, oponete)):
                            casa_verificar = f'({LinhaOrigin-2}, {ColunaOrigin+2})'
                            if (casa_verificar not in caminho):
                                cont += 1
                                caminho.append(casa_verificar)
                                return self.Prioridade_caminhos_de_comer(PosiçaoDaPedra=casa_verificar, num=cont, oponete=oponete, caminho=caminho)

                        else:
                            return cont

        if ColunaOrigin > 0 and LinhaOrigin > 0:
            if matriz[LinhaOrigin-1][ColunaOrigin-1] in oponete:
                if ColunaOrigin > 1 and LinhaOrigin > 1:
                    if matriz[LinhaOrigin-2][ColunaOrigin-2] == ' ':
                        if (self.tem_caminhos_de_comer(PosiçaoDaPedra, oponete)):
                            casa_verificar = f'({LinhaOrigin-2}, {ColunaOrigin-2})'
                            if (casa_verificar not in caminho):
                                cont += 1
                                caminho.append(casa_verificar)
                                return self.Prioridade_caminhos_de_comer(PosiçaoDaPedra=casa_verificar, num=cont, oponete=oponete, caminho=caminho)

                        else:
                            return cont
        if ColunaOrigin < 7 and LinhaOrigin < 7:

            if matriz[LinhaOrigin+1][ColunaOrigin+1] in oponete:

                if ColunaOrigin < 6 and LinhaOrigin < 6:
                    if matriz[LinhaOrigin+2][ColunaOrigin+2] == ' ':
                        if (self.tem_caminhos_de_comer(PosiçaoDaPedra, oponete)):
                            casa_verificar = f'({LinhaOrigin+2}, {ColunaOrigin+2})'
                            print(casa_verificar)
                            if (casa_verificar not in caminho):
                                caminho.append(casa_verificar)
                                cont += 1
                                return self.Prioridade_caminhos_de_comer(PosiçaoDaPedra=casa_verificar, num=cont, oponete=oponete, caminho=caminho)

                        else:
                            return cont

        if ColunaOrigin > 0 and LinhaOrigin < 7:

            if matriz[LinhaOrigin+1][ColunaOrigin-1] in oponete:
                if ColunaOrigin > 1 and LinhaOrigin < 6:
                    if matriz[LinhaOrigin+2][ColunaOrigin-2] == ' ':
                        if (self.tem_caminhos_de_comer(PosiçaoDaPedra, oponete)):
                            casa_verificar = f'({LinhaOrigin+2}, {ColunaOrigin-2})'
                            print(casa_verificar)
                            if (casa_verificar not in caminho):
                                cont += 1
                                caminho.append(casa_verificar)
                                return self.Prioridade_caminhos_de_comer(PosiçaoDaPedra=casa_verificar, num=cont, oponete=oponete, caminho=caminho)

                        else:
                            return cont
        return cont

    def tem_caminhos_de_comer_comun(self, PosiçaoDaPedra: str, oponete='Pp'):
        matriz = self.matriz
        LinhaOrigin, ColunaOrigin = int(
            PosiçaoDaPedra[1]), int(PosiçaoDaPedra[4])

        if LinhaOrigin < 7 and ColunaOrigin < 7:  # subir direita
            if matriz[LinhaOrigin-1][ColunaOrigin+1] in oponete:
                if ColunaOrigin < 6 and LinhaOrigin > 1:
                    if matriz[LinhaOrigin-2][ColunaOrigin+2] == ' ':

                        return True

        if ColunaOrigin > 0 and LinhaOrigin > 0:
            if matriz[LinhaOrigin-1][ColunaOrigin-1] in oponete:
                if ColunaOrigin > 1 and LinhaOrigin > 1:
                    if matriz[LinhaOrigin-2][ColunaOrigin-2] == ' ':
                        return True
        if ColunaOrigin < 7 and LinhaOrigin < 7:

            if matriz[LinhaOrigin+1][ColunaOrigin+1] in oponete:

                if ColunaOrigin < 6 and LinhaOrigin < 6:
                    if matriz[LinhaOrigin+2][ColunaOrigin+2] == ' ':
                        return True

        if ColunaOrigin > 0 and LinhaOrigin < 7:
            if matriz[LinhaOrigin+1][ColunaOrigin-1] in oponete:
                if ColunaOrigin > 1 and LinhaOrigin < 6:
                    if matriz[LinhaOrigin+2][ColunaOrigin-2] == ' ':
                        return True
        return False

    def Prioridade_caminhos_de_comer_pedras_dama(self, PosiçaoDaPedra: str, num=0, oponete='Pp', caminho=[]):

        matriz = self.matriz
        cont = num

        print(caminho)
        if (PosiçaoDaPedra[1] == '-' or PosiçaoDaPedra[4] == '-'):
            return cont

        LinhaOrigin, ColunaOrigin = int(
            PosiçaoDaPedra[1]), int(PosiçaoDaPedra[4])

        if matriz[LinhaOrigin][ColunaOrigin] == 'B':
            vare_cima_direita_linha = vare_cima_esquerda_linha = vare_baixo_esquerda_linha = vare_baixo_direita_linha = LinhaOrigin
            vare_cima_direita_coluna = vare_cima_esquerda_coluna = vare_baixo_esquerda_coluna = vare_baixo_direita_coluna = ColunaOrigin

            conjunto_de_pedras_posivel_jogada = LinhaOrigin, ColunaOrigin

            if ((vare_cima_direita_linha > 0) and (vare_cima_direita_coluna < 7)):  # subir para direita
                # subir para direita
                while matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == 'B' or matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':

                    # subir para direita
                    if matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':

                        casas_origin = str(
                            conjunto_de_pedras_posivel_jogada)

                        casas_jogaveis = vare_cima_direita_linha, vare_cima_direita_coluna

                        if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                casas_jogaveis]
                        else:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                casas_jogaveis]

                        if not ((vare_cima_direita_linha > 0 and vare_cima_direita_linha < 7) and (vare_cima_direita_coluna > 0 and vare_cima_direita_coluna < 7)):
                            break

                    vare_cima_direita_linha -= 1
                    vare_cima_direita_coluna += 1

            if vare_cima_esquerda_linha > 0 and vare_cima_esquerda_coluna > 0:  # subir para esqurda
                # subir para esqurda
                while matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == 'B' or matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':

                    # subir para esqurda
                    if matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':

                        casas_origin = str(
                            conjunto_de_pedras_posivel_jogada)
                        casas_jogaveis = vare_cima_esquerda_linha, vare_cima_esquerda_coluna

                        if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                casas_jogaveis]
                        else:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                casas_jogaveis]

                        if not ((vare_cima_esquerda_linha > 0 and vare_cima_esquerda_linha < 7) and (vare_cima_esquerda_coluna > 0 and vare_cima_esquerda_coluna < 7)):
                            break

                    vare_cima_esquerda_linha -= 1
                    vare_cima_esquerda_coluna -= 1

            if vare_baixo_esquerda_linha < 7 and vare_baixo_esquerda_coluna > 0:  # baixo para esqurda
                # baixo para esqurda
                while matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == 'B' or matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':

                    # baixo para esqurda
                    if matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':

                        conjunto_de_pedras_posivel_jogada = linha, coluna

                        casas_origin = str(
                            conjunto_de_pedras_posivel_jogada)

                        casas_jogaveis = vare_baixo_esquerda_linha, vare_baixo_esquerda_coluna

                        if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                casas_jogaveis]
                        else:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                casas_jogaveis]

                        if not ((vare_baixo_esquerda_linha > 0 and vare_baixo_esquerda_linha < 7) and (vare_baixo_esquerda_coluna > 0 and vare_baixo_esquerda_coluna < 7)):
                            break

                    vare_baixo_esquerda_linha += 1
                    vare_baixo_esquerda_coluna -= 1

            if vare_baixo_direita_linha < 7 and vare_baixo_direita_coluna < 7:  # baixo para direita
                # baixo para direita
                while matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == 'B' or matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':

                    # baixo para direita
                    if matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':

                        conjunto_de_pedras_posivel_jogada = linha, coluna

                        casas_origin = str(
                            conjunto_de_pedras_posivel_jogada)

                        casas_jogaveis = vare_baixo_direita_linha, vare_baixo_direita_coluna

                        if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [
                                casas_jogaveis]
                        else:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] += [
                                casas_jogaveis]

                        if not ((vare_baixo_direita_linha > 0 and vare_baixo_direita_linha < 7) and (vare_baixo_direita_coluna > 0 and vare_baixo_direita_coluna < 7)):
                            break

                    vare_baixo_direita_linha += 1
                    vare_baixo_direita_coluna += 1

        return posicoes_possiveis_das_brancas_sem_comer

    def tem_caminhos_de_comer_dama(self, PosiçaoDaPedra: str, oponete='Pp'):
        matriz = self.matriz
        posissoes_pedras_brancas_para_pretas_comer = dict()

        # if (PosiçaoDaPedra[1] == '-' or PosiçaoDaPedra[4] == '-'):
        #     return cont

        LinhaOrigin, ColunaOrigin = int(
            PosiçaoDaPedra[1]), int(PosiçaoDaPedra[4])

        if matriz[LinhaOrigin][ColunaOrigin] == 'B':  # dama
            linha1 = linha2 = linha3 = linha4 = LinhaOrigin
            coluna1 = coluna2 = coluna3 = coluna4 = ColunaOrigin

            while True:  # subir para direita
                if not ((linha1 > 0 and linha1 < 7) and (coluna1 > 0 and coluna1 < 7)):
                    break
                print('oal mundo', oponete)
                if matriz[linha1][coluna1] in oponete:  # subir para direita

                    ProLinha, ProColuna = linha1-1, coluna1+1
                    if matriz[ProLinha][ProColuna] == ' ':
                        return True

                linha1 -= 1
                coluna1 += 1
            while True:  # subir para esquerda
                if not ((linha2 > 0 and linha2 < 7) and (coluna2 > 0 and coluna2 < 7)):
                    break
                if matriz[linha2][coluna2] in oponete:  # subir para esquerda
                    if matriz[linha2-1][coluna2-1] == ' ':
                        ProLinha, ProColuna = linha2-1, coluna2-1

                        if matriz[ProLinha][ProColuna] == ' ':
                            return True

                linha2 -= 1
                coluna2 -= 1
            while True:  # decer para esquerda

                if not ((linha3 > 0 and linha3 < 7) and (coluna3 > 0 and coluna3 < 7)):
                    break
                if matriz[linha3][coluna3] in oponete:  # subir para direita

                    ProLinha, ProColuna = linha3+1, coluna3-1

                    if matriz[ProLinha][ProColuna] == ' ':
                        return True
                linha3 += 1
                coluna3 -= 1
            while True:  # decer para direita
                if not ((linha4 >= 0 and linha4 < 7) and (coluna4 >= 0 and coluna4 < 7)):
                    break
                if matriz[linha4][coluna4] in oponete:  # subir para direita

                    ProLinha, ProColuna = linha4+1, coluna4+1

                    if matriz[ProLinha][ProColuna] == ' ':
                        return True

                linha4 += 1
                coluna4 += 1

        return posissoes_pedras_brancas_para_pretas_comer

    # funçoes de açoes do tabuleiro


jogo = Dama()
print(list(jogo.pedras_brancas_dama_possiveis_de_comer().keys())[0])

casa = list(jogo.pedras_brancas_dama_possiveis_de_comer().keys())[0]


print(jogo.tem_caminhos_de_comer_dama(casa))
# print(jogo.Prioridade_caminhos_de_comer(casa))
