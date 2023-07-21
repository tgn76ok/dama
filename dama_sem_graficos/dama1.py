matriz1 = [   ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
              [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
              ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
              ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
              [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
               #0    1    2    3    4    5    6    7 
]

matriz2 = [   ['B', ' ', 'B', ' ', 'B', ' ', 'B', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
              ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
              [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
               #0    1    2    3    4    5    6    7 
]
def pedras_brancas_possiveis_de_mover_sem_comer(matriz):
    matriz = list(matriz)
    
    pedras_brancas= list()

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'b':# posiçao de todas as brancas
                
                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna                        
                            
                        if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            pedras_brancas.append(conjunto_de_pedras_posivel_jogada)
                        
                
                        
                            
                if coluna != 0 and linha != 0 :
                    if matriz[linha-1][coluna-1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna
                        
                        
                        
                        if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            pedras_brancas.append(conjunto_de_pedras_posivel_jogada)                
            elif matriz[linha][coluna] == 'B':       
                          
                vare_cima_direita_linha = linha2 = linha3 = linha4 =linha
                vare_cima_direita_coluna = coluna2 = coluna3 = coluna4 = coluna 
                
                if ((vare_cima_direita_linha >0) and (vare_cima_direita_coluna <7)):
                    #subir para direita
                    while matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == 'B' or matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':#subir para direita

                        if matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':#subir para direita

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                                
                            if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ((vare_cima_direita_linha > 0 and vare_cima_direita_linha <7) and (vare_cima_direita_coluna > 0 and vare_cima_direita_coluna <7)) :
                                break
                            
                        vare_cima_direita_linha-=1
                        vare_cima_direita_coluna+=1
                        
                        
                if linha2 >0 and coluna2 >0 :#subir para esqurda
                    while matriz[linha2][coluna2] == 'B' or matriz[linha2][coluna2] == ' ':#subir para esqurda

                        if matriz[linha2][coluna2] == ' ':#subir para esqurda

                            
                            conjunto_de_pedras_posivel_jogada = linha, coluna                       
                            
                            if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                                break
                            
                        linha2-=1
                        coluna2-=1
                if linha3 <7 and coluna3 >0 :#baixo para esqurda
                    while matriz[linha3][coluna3] == 'B' or matriz[linha3][coluna3] == ' ':#baixo para esqurda

                        if matriz[linha3][coluna3] == ' ':#baixo para esqurda
                            

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            
                            if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (linha3 > 0 and linha3 <7) and (coluna3 > 0 and coluna3 <7)) :
                                break
                            
                        linha3+=1
                        coluna3-=1
                if linha4 <7 and coluna4 <7 :#baixo para direita
                    while matriz[linha4][coluna4] == 'B' or matriz[linha4][coluna4] == ' ':#baixo para direita

                        if matriz[linha4][coluna4] == ' ':#baixo para direita
                            
                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (linha4 > 0 and linha4 <7) and (coluna4 > 0 and coluna4 <7)) :
                                break
                            
                        linha4+=1
                        coluna4+=1
                        
                        
                        
    return pedras_brancas


def jogar():
    turno = 0
    for i in range(len(matriz1[0])):  
        if matriz1[0][i] == 'b':matriz1[0][i] ='B'
        
        
    for i in range(len(matriz1[7])):  
        if matriz1[7][i] == 'p':matriz1[7][i] ='P'   
        
        
    pedras =pedras_brancas_possiveis_de_mover_sem_comer(matriz2)
    
    print(pedras)
        
    while True:
        
        turno += 1
        
        if turno % 2 ==0 :
            pass
            #turno das bancas
        else:
            pass
            #turno das pretas
    
    
if __name__ == '__main__':
    jogar()