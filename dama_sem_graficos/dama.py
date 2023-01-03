import os 
matriz1 = [   [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],
              ['b', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
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
                          
                linha1 = linha2 = linha3 = linha4 =linha
                coluna1 = coluna2 = coluna3 = coluna4 = coluna 
                
                if linha1 >0 and coluna1 <7:#subir para direita
                    while matriz[linha1][coluna1] == 'B' or matriz[linha1][coluna1] == ' ':#subir para direita

                        if matriz[linha1][coluna1] == ' ':#subir para direita

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                                
                            if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                                break
                            
                        linha1-=1
                        coluna1+=1
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

def posiçoes_possiveis_brancas(matriz,posçoes_da_pedra):
    
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    posicoes_possiveis_das_brancas = list()
    
    if matriz[linha][coluna] == 'b':# posiçao de todas as brancas
        
        if coluna != 7 and linha != 0 :
            if matriz[linha-1][coluna+1] == ' ':
                
                
                conjunto_de_jogadas = linha-1,coluna+1
                if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                    posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)
                    
                
        if coluna != 0 and linha != 0:
            if matriz[linha-1][coluna-1] == ' ':
                
                
                
                conjunto_de_jogadas = linha-1,coluna-1
                if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                    posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)
    elif matriz[linha][coluna] == 'B': 
          
        linha1 = linha2 = linha3 = linha4 =linha
        coluna1 = coluna2 = coluna3 = coluna4 = coluna 
        if linha1 >0 and coluna1 <7:
            while matriz[linha1][coluna1] == 'B' or matriz[linha1][coluna1] == ' ':

                if matriz[linha1][coluna1] == ' ':#subir para direita
                    

                    
                    conjunto_de_jogadas = linha1,coluna1
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                        posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

                    
                    if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                        break
                    
                linha1-=1
                coluna1+=1
        if linha2 >0 and coluna2 >0 :
            while matriz[linha2][coluna2] == 'B' or matriz[linha2][coluna2] == ' ':

                if matriz[linha2][coluna2] == ' ':#subir para esqurda

                    
                    conjunto_de_jogadas = linha2,coluna2
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                        posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

                    
                    if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                        break
                    
                linha2-=1
                coluna2-=1
        if linha3 <7 and coluna3 >0 :
            while matriz[linha3][coluna3] == 'B' or matriz[linha3][coluna3] == ' ':

                if matriz[linha3][coluna3] == ' ':#baixo para esqurda
                    

                    conjunto_de_jogadas = linha3,coluna3
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                        posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

                    
                    if not ( (linha3 > 0 and linha3 <7) and (coluna3 > 0 and coluna3 <7)) :
                        break
                    
                linha3+=1
                coluna3-=1
        if linha4 <7 and coluna4 <7 :
            
            while matriz[linha4][coluna4] == 'B' or matriz[linha4][coluna4] == ' ':

                if matriz[linha4][coluna4] == ' ':#baixo para direita
                    

                    
                    conjunto_de_jogadas = linha4,coluna4
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                        posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

                    
                    if not ( (linha4 > 0 and linha4 <7) and (coluna4 > 0 and coluna4 <7)) :
                        break
                    
                linha4+=1
                coluna4+=1
    else:   
        print("erro essa pedra nao é branca")
        exit()             
                                       
                 
                        
    return posicoes_possiveis_das_brancas
    

def pedras_pretas_possiveis_de_mover_sem_comer(matriz):
    
    matriz = list(matriz)
    pedras_pretas= list()
    
    
    posicoes_possiveis_das_pretas = list()
    for linha in range(len(matriz1)):
        for coluna in range(len(matriz1)):
            if matriz1[linha][coluna] == 'p':# posiçao de todas as pretas
                
                if coluna != 0 and linha != 7:
                    if matriz1[linha+1][coluna-1] == ' ':

                        conjunto_de_pedras_posivel_jogada = linha, coluna


                        conjunto_de_jogadas = linha+1,coluna-1
                        if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                            posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)
                            
                            
                        if conjunto_de_pedras_posivel_jogada not in pedras_pretas:
                            pedras_pretas.append(conjunto_de_pedras_posivel_jogada)
                
                 
                if coluna != 7 and linha !=7 :
                    if matriz1[linha+1][coluna+1] == ' ':

                        conjunto_de_pedras_posivel_jogada = linha, coluna


                        conjunto_de_jogadas = linha+1,coluna+1
                        
                        if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                            posicoes_possiveis_das_pretas.append(conjunto_de_jogadas) 

                        if conjunto_de_pedras_posivel_jogada not in pedras_pretas:
                            pedras_pretas.append(conjunto_de_pedras_posivel_jogada)        
            elif matriz1[linha][coluna] == 'P':                           
               
                linha1 = linha2 = linha3 = linha4 =linha
                coluna1 = coluna2 = coluna3 = coluna4 = coluna
                       
                 
                if linha1 >0 and coluna1 <7:
                    while matriz[linha1][coluna1] == 'P' or matriz[linha1][coluna1] == ' ':#subir para direita

                        if matriz[linha1][coluna1] == ' ':

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                                
                            if conjunto_de_pedras_posivel_jogada not in pedras_pretas:
                                pedras_pretas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                                break
                            
                        linha1-=1
                        coluna1+=1
                if linha2 >0 and coluna2 >0:
                    while matriz[linha2][coluna2] == 'P' or matriz[linha2][coluna2] == ' ':#subir para esqurda

                        if matriz[linha2][coluna2] == ' ':

                            
                            conjunto_de_pedras_posivel_jogada = linha, coluna                       
                            
                            if conjunto_de_pedras_posivel_jogada not in pedras_pretas:
                                pedras_pretas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                                break
                            
                        linha2-=1
                        coluna2-=1
                if linha3 <7 and coluna3 >0:
                    while matriz[linha3][coluna3] == 'P' or matriz[linha3][coluna3] == ' ':

                        if matriz[linha3][coluna3] == ' ':#baixo para esqurda
                            

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            
                            if conjunto_de_pedras_posivel_jogada not in pedras_pretas:
                                pedras_pretas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (linha3 > 0 and linha3 <7) and (coluna3 > 0 and coluna3 <7)) :
                                break
                            
                        linha3+=1
                        coluna3-=1
                if linha4 <7 and coluna4 <7:
                    while matriz[linha4][coluna4] == 'P' or matriz[linha4][coluna4] == ' ':
                        

                        if matriz[linha4][coluna4] == ' ':#baixo para direita
                            
                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            if conjunto_de_pedras_posivel_jogada not in pedras_pretas:
                                pedras_pretas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (linha4 > 0 and linha4 <7) and (coluna4 > 0 and coluna4 <7)) :
                                break
                            
                        linha4+=1
                        coluna4+=1
                            
                               
    return pedras_pretas

def posiçoes_possiveis_pretas(matriz,posçoes_da_pedra):
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    
    posicoes_possiveis_das_pretas = list()
    
    if matriz[linha][coluna] == 'p':# posiçao de todas as pretas
        
        if coluna != 7 :
            if matriz[linha+1][coluna+1] == ' ':
                
                
                conjunto_de_jogadas = linha+1,coluna+1
                if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                    posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)
                    
                
        if coluna != 0:
            if matriz[linha+1][coluna-1] == ' ':
                
                
                
                conjunto_de_jogadas = linha+1,coluna-1
                if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                    posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)
    elif matriz[linha][coluna] == 'P': 
          
        linha1 = linha2 = linha3 = linha4 =linha
        coluna1 = coluna2 = coluna3 = coluna4 = coluna 
        
        if linha1 >0 and coluna1 <7:

            while matriz[linha1][coluna1] == 'P' or matriz[linha1][coluna1] == ' ':

                if matriz[linha1][coluna1] == ' ':#subir para direita
                    

                    
                    conjunto_de_jogadas = linha1,coluna1
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                        posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)

                    
                    if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                        break
                    
                linha1-=1
                coluna1+=1
        if linha2 >0 and coluna2 >0:
            while matriz[linha2][coluna2] == 'P' or matriz[linha2][coluna2] == ' ':

                if matriz[linha2][coluna2] == ' ':#subir para esqurda

                    
                    conjunto_de_jogadas = linha2,coluna2
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                        posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)

                    
                    if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                        break
                    
                linha2-=1
                coluna2-=1
        if linha3 <7 and coluna3 >0:
            while matriz[linha3][coluna3] == 'P' or matriz[linha3][coluna3] == ' ':

                if matriz[linha3][coluna3] == ' ':#baixo para esqurda
                    

                    conjunto_de_jogadas = linha3,coluna3
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                        posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)

                    
                    if not ( (linha3 > 0 and linha3 <7) and (coluna3 > 0 and coluna3 <7)) :
                        break
                    
                linha3+=1
                coluna3-=1
        if linha4 <7 and coluna4 <7:
            while matriz[linha4][coluna4] == 'P' or matriz[linha4][coluna4] == ' ':

                if matriz[linha4][coluna4] == ' ':#baixo para direita
                    

                    
                    conjunto_de_jogadas = linha4,coluna4
                    if conjunto_de_jogadas  not in  posicoes_possiveis_das_pretas:
                        posicoes_possiveis_das_pretas.append(conjunto_de_jogadas)

                    
                    if not ( (linha4 > 0 and linha4 <7) and (coluna4 > 0 and coluna4 <7)) :
                        break
                    
                linha4+=1
                coluna4+=1
    else:
        print("erro essa pedra nao é pretas")
        exit()             
                                       
                 
                        
    return posicoes_possiveis_das_pretas

def pode_comer_para_brancas(matriz):
    matriz = list(matriz)
    
    pedras_brancas_possiveis_de_comer= list()
    

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'b':# posiçao de todas as brancas

                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] in 'pP':
                        if coluna != 6 and linha != 1:
                            if matriz[linha-2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
      
                if coluna != 0 and linha != 0:
                    if matriz[linha-1][coluna-1] in 'pP':
                        if coluna != 1 and linha != 1:
                            if matriz[linha-2][coluna-2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                if coluna != 7 and linha != 7:
                    
                    if matriz[linha+1][coluna+1]  in 'pP':
                        
                        if coluna != 6 and linha != 6:
                            if matriz[linha+2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 0 and linha != 7:
                    if matriz[linha+1][coluna-1] in 'pP' :
                        if coluna != 1 and linha != 6:
                            if matriz[linha+2][coluna-2] ==' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
            elif matriz[linha][coluna] == 'B':
                linha1 = linha2 = linha3 = linha4 =linha
                coluna1 = coluna2 = coluna3 = coluna4 = coluna 

                while True:#subir para direita 
                    if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                            break
                    if matriz[linha1][coluna1] in'Pp':#subir para direita       
                        if matriz[linha1-1][coluna1+1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                    linha1-=1
                    coluna1+=1
                while True:#subir para esquerda
                    if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                            break
                    if matriz[linha2][coluna2] in 'pP':#subir para esquerda       
                        if matriz[linha2-1][coluna2-1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                    linha2-=1
                    coluna2-=1
                while True:#decer para esquerda
                    
                    if not ( (0<=linha3<7) and (0<coluna3<=7)) :
                            break
                    
                    if matriz[linha3][coluna3] in 'pP':#decer para esqerda    
                          
                        if matriz[linha3+1][coluna3-1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                    linha3+=1
                    coluna3-=1
                while True:#decer para direita
                    if not ( (linha4 >= 0 and linha4 <7) and (coluna4 >= 0 and coluna4 <7)) :
                            break
                    if matriz[linha4][coluna4] in 'pP':#subir para direita       
                        if matriz[linha4+1][coluna4+1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                    linha4+=1
                    coluna4+=1   
                
    return pedras_brancas_possiveis_de_comer  
        
def posiçoes_possiveis_para_comer_brancas(matriz,posçoes_da_pedra):
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    pedras_brancas_posisao_de_comer= list()
    pedras_pretas_para_apagar= list()



    if matriz[linha][coluna] == 'b':# posiçao de todas as brancas

        if coluna != 7 and linha != 0 :
            if matriz[linha-1][coluna+1] in 'pP':
                if coluna != 6 and linha != 1:
                    if matriz[linha-2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                            pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

        if coluna != 0 and linha != 0:
            if matriz[linha-1][coluna-1] in 'pP':
                if coluna != 1 and linha != 1:
                    if matriz[linha-2][coluna-2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna-2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                            pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 7 and linha != 7:
            if matriz[linha+1][coluna+1] in 'pP':
                if coluna != 6 and linha != 6:
                    if matriz[linha+2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                            pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 0 and linha != 7:
            if matriz[linha+1][coluna-1] in 'pP':
                if coluna != 1 and linha != 6:
                    if matriz[linha+2][coluna-2] ==' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna-2
                        
                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                            pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                            
    elif matriz[linha][coluna] == 'B':
                linha1 = linha2 = linha3 = linha4 =linha
                coluna1 = coluna2 = coluna3 = coluna4 = coluna 

                while True:#subir para direita 
                    if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                            break
                    if matriz[linha1][coluna1] in 'pP':#subir para direita       
                        if matriz[linha1-1][coluna1+1] == ' ':               
                            
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha1-1, coluna1+1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                                pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha1, coluna1

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                                pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

                        
                        
                    linha1-=1
                    coluna1+=1
                while True:#subir para esquerda
                    if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                            break
                    if matriz[linha2][coluna2] in 'pP':#subir para esquerda       
                        if matriz[linha2-1][coluna2-1] == ' ':               
                            
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha2-1, coluna2-1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                                pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha2, coluna2

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                                pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
        
                        
                    linha2-=1
                    coluna2-=1
                while True:#decer para esquerda
                    if not ( (0<=linha3<7) and (0<coluna3<=7)) :
                            break
                    if matriz[linha3][coluna3] in 'pP':#decer para esqerda      
                        if matriz[linha3+1][coluna3-1] == ' ':               
                            
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha3+1, coluna3-1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                                pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha3, coluna3

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                                pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

                        
                    linha3+=1
                    coluna3-=1
                while True:#decer para direita
                    
                    if not ( (0<=linha4<7) and (0<=coluna4<7)) :
                            break
                    if matriz[linha4][coluna4] in 'pP':#subir para direita       
                        if matriz[linha4+1][coluna4+1] == ' ':               
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha4+1, coluna4+1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                                pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha4, coluna4

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_pretas_para_apagar:
                                pedras_pretas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)


                        
                        
                    linha4+=1
                    coluna4+=1   
                
        
    return (pedras_brancas_posisao_de_comer,pedras_pretas_para_apagar)
                                                
def pode_comer_para_pretas(matriz):
    matriz = list(matriz)
    
    pedras_pretas_possiveis_de_comer= list()
    

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'p':# posiçao de todas as pretas

                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] in 'Bb':
                        if coluna != 6 and linha != 1:
                            if matriz[linha-2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
      
                if coluna != 0 and linha != 0:
                    if matriz[linha-1][coluna-1] in 'Bb':
                        if coluna != 1 and linha != 1:
                            if matriz[linha-2][coluna-2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 7 and linha != 7:
                    if matriz[linha+1][coluna+1] in 'Bb':
                        if coluna != 6 and linha != 6:
                            if matriz[linha+2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 0 and linha != 7:
                    if matriz[linha+1][coluna-1] in 'Bb':
                        if coluna != 1 and linha != 6:
                            if matriz[linha+2][coluna-2] ==' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
            elif matriz[linha][coluna] == 'P':
                linha1 = linha2 = linha3 = linha4 =linha
                coluna1 = coluna2 = coluna3 = coluna4 = coluna 
                while True :#subir para direita 
                    linha1-=1
                    coluna1+=1
                    if  not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                            break
                    if matriz[linha1][coluna1] in 'Bb':#subir para direita  
                             
                        if matriz[linha1-1][coluna1+1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_pretas_possiveis_de_comer:
                                pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                    
                while True:#subir para esquerda
                    linha2-=1
                    coluna2-=1
                    if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                            break
                    if matriz[linha2][coluna2] in 'Bb':#subir para esquerda       
                        if matriz[linha2-1][coluna2-1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_pretas_possiveis_de_comer:
                                pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                while True:#decer para esquerda
                    linha3+=1
                    coluna3-=1
                    if not ( (linha3 > 0 and linha3 <7) and (coluna3 > 0 and coluna3 <7)) :
                            break
                    if matriz[linha3][coluna3] in 'Bb':#decer para esqerda      
                        if matriz[linha3+1][coluna3-1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_pretas_possiveis_de_comer:
                                pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

                        
                        
                    
                while True:#decer para direita
                    linha4+=1
                    coluna4+=1  
                    
                    
                    if  not ((0 < linha4 < 7) and (0 < coluna4 < 7)) :
                        
                        break
                    
                    
                    
                   
                        
                        
                    if matriz[linha4][coluna4] in 'Bb' and (linha4 > 1 and linha4 < 6) or (coluna4 > 1 and coluna4 <6):#subir para direita       
                        if matriz[linha4+1][coluna4+1] == ' ':               
                            
                            
                            conjunto_de_pedras_posivel_de_comer = linha,coluna
                            if conjunto_de_pedras_posivel_de_comer  not in  pedras_pretas_possiveis_de_comer:
                                pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                    

                        
                        
                    
                
                
    return pedras_pretas_possiveis_de_comer  
        
def posiçoes_possiveis_para_comer_pretas(matriz,posçoes_da_pedra):
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    pedras_pretas_posisao_de_comer= list()
    pedras_brancas_para_apagar= list()



    if matriz[linha][coluna] == 'p':# posiçao de todas as brancas

        if coluna != 7 and linha != 0 :
            if matriz[linha-1][coluna+1] in 'bB':
                if coluna != 6 and linha != 1:
                    if matriz[linha-2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                            pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

        if coluna != 0 and linha != 0:
            if matriz[linha-1][coluna-1] in 'bB':
                if coluna != 1 and linha != 1:
                    if matriz[linha-2][coluna-2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna-2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                            pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 7 and linha != 7:
            if matriz[linha+1][coluna+1] in 'bB':
                if coluna != 6 and linha != 6:
                    if matriz[linha+2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                            pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 0 and linha != 7:
            if matriz[linha+1][coluna-1] in 'bB':
                if coluna != 1 and linha != 6:
                    if matriz[linha+2][coluna-2] ==' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna-2
                        
                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                            pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
    elif matriz[linha][coluna] == 'P':
                linha1 = linha2 = linha3 = linha4 =linha
                coluna1 = coluna2 = coluna3 = coluna4 = coluna 

                while True:#subir para direita
                    linha1-=1
                    coluna1+=1 
                    if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                            break
                    if matriz[linha1][coluna1] in 'Bb':#subir para direita       
                        if matriz[linha1-1][coluna1+1] == ' ':               
                            
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha1-1, coluna1+1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                                pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha1, coluna1

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                                pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

                        
                        
                    
                while True:#subir para esquerda
                    linha2-=1
                    coluna2-=1
                    if not ( (linha2 > 0 and linha2 <7) and (coluna2 > 0 and coluna2 <7)) :
                            break
                    if matriz[linha2][coluna2] in 'Bb':#subir para esquerda       
                        if matriz[linha2-1][coluna2-1] == ' ':               
                            
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha2-1, coluna2-1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                                pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha2, coluna2

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                                pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
        
                        
                    
                while True:#decer para esquerda
                    linha3+=1
                    coluna3-=1
                    if not ( (linha3 > 0 and linha3 <7) and (coluna3 > 0 and coluna3 <7)) :
                            break
                    if matriz[linha3][coluna3] in 'Bb':#decer para esqerda      
                        if matriz[linha3+1][coluna3-1] == ' ':               
                            
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha3+1, coluna3-1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                                pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha3, coluna3

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                                pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

                        
                    
                while True:#decer para direita
                    linha4+=1
                    coluna4+=1
                    
                    if  not (linha4 > 0 and linha4 < 7) or (coluna4 > 0 and coluna4 <7) :
                            break
                    if matriz[linha4][coluna4] in 'Bb':#subir para direita       
                        if matriz[linha4+1][coluna4+1] == ' ' and (linha4 > 1 and linha4 < 7) or (coluna4 > 0 and coluna4 <7):               
                            conjunto_de_posiçoes_pedras_posivel_de_comer = linha4+1, coluna4+1
                        
                            if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_pretas_posisao_de_comer:
                                pedras_pretas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                                
                            conjunto_de_posiçoes_pedras_para_apagar = linha4, coluna4

                            if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                                pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)


                        
                        
   
                
                      
                        
        
    return (pedras_pretas_posisao_de_comer,pedras_brancas_para_apagar)


ja_comeu=False
turno = 1
cont = 0


while True:
    
    for i in range(len(matriz1[0])):  
        if matriz1[0][i] == 'b':matriz1[0][i] ='B'
        
        
    for i in range(len(matriz1[7])):  
        if matriz1[7][i] == 'p':matriz1[7][i] ='P'   
         
    pedra_para_comer_preta = pode_comer_para_pretas(matriz1)
    
    pedra_para_comer_branca = pode_comer_para_brancas(matriz1)

    
    print(f"-------------------------------------------")
    print(f"{matriz1[0]}\n{matriz1[1]}\n{matriz1[2]}\n{matriz1[3]}\n{matriz1[4]}\n{matriz1[5]}\n{matriz1[6]}\n{matriz1[7]}\n")
    if turno %2 ==0:#brancas
        if len(pedra_para_comer_branca) ==0:
            
 
            pedras_brancas = pedras_brancas_possiveis_de_mover_sem_comer(matriz1) 
            
            print(f"Escolha uma das pedras brancas, pelo numero com respodente")
            for i in pedras_brancas: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont= 0
            
            index_para_pegar_a_pedra= int(input(">>"))
            pedra_escolhida_pelo_jogador_1=pedras_brancas[index_para_pegar_a_pedra]
            posiçao_das_posiveis_jogadas = posiçoes_possiveis_brancas(matriz1,pedra_escolhida_pelo_jogador_1)
            
            
            print("agora escolha aonde voce quer jogar andar")
            for i in posiçao_das_posiveis_jogadas: print(f"{cont}. posiçao-{i}"); cont+=1 
            
            cont = 0 
            index_para_pegar_a_jogada= int(input(">>"))
            jogada_escolhida_pelo_jogador_1=posiçao_das_posiveis_jogadas[index_para_pegar_a_jogada]
            
            pedra_branca = 'b' if matriz1[pedra_escolhida_pelo_jogador_1[0]][pedra_escolhida_pelo_jogador_1[1]]== 'b' else 'B'
            
            matriz1[pedra_escolhida_pelo_jogador_1[0]][pedra_escolhida_pelo_jogador_1[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_1[0]][jogada_escolhida_pelo_jogador_1[1]]= pedra_branca

            turno+=1
    
        else:#brancas obrigaorio comer
            print(f"Escolha uma das pedras brancas para comer outra preta, pelo numero com respodente")
            for i in pedra_para_comer_branca: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont = 0 
            
            
            index_para_pegar_a_pedra= int(input(">>"))
            pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1=pedra_para_comer_branca[index_para_pegar_a_pedra]
            posiçao_das_posiveis_jogadas_para_comer,pedras_pretas_para_apagar = posiçoes_possiveis_para_comer_brancas(matriz1,pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1)
            
            print("agora escolha aonde voce quer jogar")
            for i in posiçao_das_posiveis_jogadas_para_comer: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont = 0 
            
            
            index_para_pegar_a_jogada= int(input(">>"))
            jogada_escolhida_pelo_jogador_1_para_comer=posiçao_das_posiveis_jogadas_para_comer[index_para_pegar_a_jogada]
            pedra_escolhida_para_apagar = pedras_pretas_para_apagar[index_para_pegar_a_jogada]
            
            pedra_branca = 'b' if matriz1[pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1[0]][pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1[1]] == 'b' else 'B'
            
            matriz1[pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1[0]][pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1[1]]= ' '
            matriz1[pedra_escolhida_para_apagar[0]][pedra_escolhida_para_apagar[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_1_para_comer[0]][jogada_escolhida_pelo_jogador_1_para_comer[1]]= pedra_branca
            ja_comeu=True
        
            
    else:#pretas
        
        if len(pedra_para_comer_preta) == 0:
            

            pedras_pretas = pedras_pretas_possiveis_de_mover_sem_comer(matriz1)


            print(f"Escolha uma das pedras pretas para andar, pelo numero conrespodente")
            for i in pedras_pretas: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont= 0
            
            index_para_pegar_a_pedra= int(input(">>"))
            pedra_escolhida_pelo_jogador_2=pedras_pretas[index_para_pegar_a_pedra]
            posiçao_das_posiveis_jogadas = posiçoes_possiveis_pretas(matriz1,pedra_escolhida_pelo_jogador_2)
            
            
            print("agora escolha aonde voce quer jogar")
            for i in posiçao_das_posiveis_jogadas: print(f"{cont}. posiçao-{i}"); cont+=1 
            
            cont = 0 
            index_para_pegar_a_jogada= int(input(">>"))
            jogada_escolhida_pelo_jogador_2=posiçao_das_posiveis_jogadas[index_para_pegar_a_jogada]
            pedra_preta ='p' if matriz1[pedra_escolhida_pelo_jogador_2[0]][pedra_escolhida_pelo_jogador_2[1]] == 'p' else 'P'
            matriz1[pedra_escolhida_pelo_jogador_2[0]][pedra_escolhida_pelo_jogador_2[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_2[0]][jogada_escolhida_pelo_jogador_2[1]]= pedra_preta

            turno+=1

            
        else:#pretas obrigatorio comer
            print(f"Escolha uma das pedras para comer uma branca, pelo numero com respodente 3")
            for i in pedra_para_comer_preta: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont = 0 
            
            
            index_para_pegar_a_pedra= int(input(">>"))
            pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2=pedra_para_comer_preta[index_para_pegar_a_pedra]
            
            posiçao_das_posiveis_jogadas_para_comer_pretas,pedras_brancas_para_apagar = posiçoes_possiveis_para_comer_pretas(matriz1,pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2)
            
            print("agora escolha aonde voce quer jogar")
            
            for i in posiçao_das_posiveis_jogadas_para_comer_pretas: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont = 0 
            
            
            index_para_pegar_a_jogada= int(input(">>"))
            jogada_escolhida_pelo_jogador_2_para_comer=posiçao_das_posiveis_jogadas_para_comer_pretas[index_para_pegar_a_jogada]
            pedra_escolhida_para_apagar = pedras_brancas_para_apagar[index_para_pegar_a_jogada]
            pedra_preta = 'p' if matriz1[pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2[0]][pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2[1]] == 'p' else 'P'
            matriz1[pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2[0]][pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2[1]]= ' '
            matriz1[pedra_escolhida_para_apagar[0]][pedra_escolhida_para_apagar[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_2_para_comer[0]][jogada_escolhida_pelo_jogador_2_para_comer[1]]= pedra_preta
            ja_comeu=True

    