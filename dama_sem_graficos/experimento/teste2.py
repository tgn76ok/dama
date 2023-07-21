
matriz = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#0
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#1
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#2
              [' ', ' ', ' ', 'p', ' ', ' ', ' ', ' '],#3
              [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],#4
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#5
              [' ', ' ', ' ', ' ', ' ', 'P', ' ', ' '],#6
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#7
               #0    1    2    3    4    5    6    7 
]



# funçoes de status do tabuleiro 
def pedras_brancas_possiveis_de_mover_sem_comer(matriz):
    matriz = list(matriz)
    
    posicoes_possiveis_das_brancas_sem_comer={}

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'b':# posiçao de todas as brancas
                
                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna                        
                            
                        casas_origin = str(conjunto_de_pedras_posivel_jogada) 
                        
                        casas_jogaveis = linha-1 , coluna+1
    
                        if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [casas_jogaveis]
                        else:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                        
                
                        
                            
                if coluna != 0 and linha != 0 :
                    if matriz[linha-1][coluna-1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna
                        
                        
                        
                        casas_origin = str(conjunto_de_pedras_posivel_jogada) 
                        
                        casas_jogaveis = linha-1 , coluna+1
    
                        if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [casas_jogaveis]
                        else:
                            posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [casas_jogaveis]            
         
         
            elif matriz[linha][coluna] == 'B':       
                          
                vare_cima_direita_linha = vare_cima_esquerda_linha = vare_baixo_esquerda_linha = vare_baixo_direita_linha =linha
                vare_cima_direita_coluna = vare_cima_esquerda_coluna = vare_baixo_esquerda_coluna = vare_baixo_direita_coluna = coluna 
                
                conjunto_de_pedras_posivel_jogada = linha, coluna
                
                if ((vare_cima_direita_linha >0) and (vare_cima_direita_coluna <7)):#subir para direita
                    #subir para direita
                    while matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == 'B' or matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':#subir para direita

                        if matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':#subir para direita

                                
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                
                            casas_origin = str(conjunto_de_pedras_posivel_jogada) 
                            
                            casas_jogaveis = vare_cima_direita_linha,vare_cima_direita_coluna
        
                            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                                
                            # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ((vare_cima_direita_linha > 0 and vare_cima_direita_linha <7) and (vare_cima_direita_coluna > 0 and vare_cima_direita_coluna <7)) :
                                break
                            
                        vare_cima_direita_linha-=1
                        vare_cima_direita_coluna+=1
                        
                        
                if vare_cima_esquerda_linha >0 and vare_cima_esquerda_coluna >0 :#subir para esqurda
                    while matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == 'B' or matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':#subir para esqurda

                        if matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':#subir para esqurda

                            
                            
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            
                            casas_origin = str(conjunto_de_pedras_posivel_jogada)                             
                            casas_jogaveis = vare_cima_esquerda_linha, vare_cima_esquerda_coluna
        
                            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                                
                                # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (vare_cima_esquerda_linha > 0 and vare_cima_esquerda_linha <7) and (vare_cima_esquerda_coluna > 0 and vare_cima_esquerda_coluna <7)) :
                                break
                            
                        vare_cima_esquerda_linha-=1
                        vare_cima_esquerda_coluna-=1
                
                if vare_baixo_esquerda_linha <7 and vare_baixo_esquerda_coluna >0 :#baixo para esqurda
                    while matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == 'B' or matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':#baixo para esqurda

                        if matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':#baixo para esqurda
                            

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                
                            casas_origin = str(conjunto_de_pedras_posivel_jogada)                             
                            
                            casas_jogaveis = vare_baixo_esquerda_linha, vare_baixo_esquerda_coluna
        
                            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [casas_jogaveis]
                                # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (vare_baixo_esquerda_linha > 0 and vare_baixo_esquerda_linha <7) and (vare_baixo_esquerda_coluna > 0 and vare_baixo_esquerda_coluna <7)) :
                                break
                            
                        vare_baixo_esquerda_linha+=1
                        vare_baixo_esquerda_coluna-=1
                
                
                if vare_baixo_direita_linha <7 and vare_baixo_direita_coluna <7 :#baixo para direita
                    while matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == 'B' or matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':#baixo para direita

                        if matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':#baixo para direita
                            
                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            
                            casas_origin = str(conjunto_de_pedras_posivel_jogada)  
                            
                            casas_jogaveis = vare_baixo_direita_linha,vare_baixo_direita_coluna
        
                            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                                # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (vare_baixo_direita_linha > 0 and vare_baixo_direita_linha <7) and (vare_baixo_direita_coluna > 0 and vare_baixo_direita_coluna <7)) :
                                break
                            
                        vare_baixo_direita_linha+=1
                        vare_baixo_direita_coluna+=1
                        
                        
                        
    return posicoes_possiveis_das_brancas_sem_comer

def pedras_pretas_possiveis_de_mover_sem_comer(matriz):
    matriz = list(matriz)
    
    posicoes_possiveis_das_pretas_sem_comer={}

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'p':# posiçao de todas as pretas
                
                if coluna != 0 and linha != 7:
                    if matriz[linha+1][coluna-1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna                        
                            
                        casas_origin = str(conjunto_de_pedras_posivel_jogada) 
                        
                        casas_jogaveis = linha-1 , coluna+1
    
                        if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [casas_jogaveis]
                        else:
                            posicoes_possiveis_das_pretas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                        
                
                        
                            
                if coluna != 7 and linha !=7 :

                    if matriz[linha+1][coluna+1]== ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna
                        
                        
                        
                        casas_origin = str(conjunto_de_pedras_posivel_jogada) 
                        
                        casas_jogaveis = linha+1 , coluna+1
    
                        if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                            posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [casas_jogaveis]
                        else:
                            posicoes_possiveis_das_pretas_sem_comer[casas_origin]+= [casas_jogaveis]            
         
         
            elif matriz[linha][coluna] == 'P':       
                          
                vare_cima_direita_linha = vare_cima_esquerda_linha = vare_baixo_esquerda_linha = vare_baixo_direita_linha =linha
                vare_cima_direita_coluna = vare_cima_esquerda_coluna = vare_baixo_esquerda_coluna = vare_baixo_direita_coluna = coluna 
                
                conjunto_de_pedras_posivel_jogada = linha, coluna
                
                if ((vare_cima_direita_linha >0) and (vare_cima_direita_coluna <7)):#subir para direita
                    #subir para direita
                    while matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == 'P' or matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':#subir para direita

                        if matriz[vare_cima_direita_linha][vare_cima_direita_coluna] == ' ':#subir para direita

                                
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                
                            casas_origin = str(conjunto_de_pedras_posivel_jogada) 
                            
                            casas_jogaveis = vare_cima_direita_linha,vare_cima_direita_coluna
        
                            if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                                
                            # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ((vare_cima_direita_linha > 0 and vare_cima_direita_linha <7) and (vare_cima_direita_coluna > 0 and vare_cima_direita_coluna <7)) :
                                break
                            
                        vare_cima_direita_linha-=1
                        vare_cima_direita_coluna+=1
                        
                        
                if vare_cima_esquerda_linha >0 and vare_cima_esquerda_coluna >0 :#subir para esqurda
                    while matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == 'P' or matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':#subir para esqurda

                        if matriz[vare_cima_esquerda_linha][vare_cima_esquerda_coluna] == ' ':#subir para esqurda

                            
                            
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            
                            casas_origin = str(conjunto_de_pedras_posivel_jogada)                             
                            casas_jogaveis = vare_cima_esquerda_linha, vare_cima_esquerda_coluna
        
                            if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                                
                                # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (vare_cima_esquerda_linha > 0 and vare_cima_esquerda_linha <7) and (vare_cima_esquerda_coluna > 0 and vare_cima_esquerda_coluna <7)) :
                                break
                            
                        vare_cima_esquerda_linha-=1
                        vare_cima_esquerda_coluna-=1
                
                if vare_baixo_esquerda_linha <7 and vare_baixo_esquerda_coluna >0 :#baixo para esqurda
                    while matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == 'P' or matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':#baixo para esqurda

                        if matriz[vare_baixo_esquerda_linha][vare_baixo_esquerda_coluna] == ' ':#baixo para esqurda
                            

                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                                
                            casas_origin = str(conjunto_de_pedras_posivel_jogada)                             
                            
                            casas_jogaveis = vare_baixo_esquerda_linha, vare_baixo_esquerda_coluna
        
                            if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin]+= [casas_jogaveis]
                                # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (vare_baixo_esquerda_linha > 0 and vare_baixo_esquerda_linha <7) and (vare_baixo_esquerda_coluna > 0 and vare_baixo_esquerda_coluna <7)) :
                                break
                            
                        vare_baixo_esquerda_linha+=1
                        vare_baixo_esquerda_coluna-=1
                
                
                if vare_baixo_direita_linha <7 and vare_baixo_direita_coluna <7 :#baixo para direita
                    while matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == 'P' or matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':#baixo para direita

                        if matriz[vare_baixo_direita_linha][vare_baixo_direita_coluna] == ' ':#baixo para direita
                            
                            conjunto_de_pedras_posivel_jogada = linha, coluna
                            
                            # if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            
                            casas_origin = str(conjunto_de_pedras_posivel_jogada)  
                            
                            casas_jogaveis = vare_baixo_direita_linha,vare_baixo_direita_coluna
        
                            if posicoes_possiveis_das_pretas_sem_comer.get(casas_origin) is None:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin] = [casas_jogaveis]
                            else:
                                posicoes_possiveis_das_pretas_sem_comer[casas_origin]+= [casas_jogaveis]
                                
                                # pedras_brancas.append(conjunto_de_pedras_posivel_jogada)

                            
                            if not ( (vare_baixo_direita_linha > 0 and vare_baixo_direita_linha <7) and (vare_baixo_direita_coluna > 0 and vare_baixo_direita_coluna <7)) :
                                break
                            
                        vare_baixo_direita_linha+=1
                        vare_baixo_direita_coluna+=1
                        
                        
                        
    return posicoes_possiveis_das_pretas_sem_comer

def pedras_brancas_possiveis_de_mover_comendo_comun(matriz):
     
    pedras_brancas_possiveis_de_comer= dict()
    

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'b':# posiçao de todas as brancas

                if coluna < 7 and linha > 0 :#subir direita
                    if matriz[linha-1][coluna+1] in 'pP':
                        if coluna < 6 and linha > 1:
                            if matriz[linha-2][coluna+2] == ' ':
                                print("a")
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                    
                                casas_origin = str(conjunto_de_pedras_posivel_de_comer) 
                    
                                casas_jogaveis = linha-2 , coluna+2
            
                                if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                    pedras_brancas_possiveis_de_comer[casas_origin] = [casas_jogaveis]
                                else:
                                    pedras_brancas_possiveis_de_comer[casas_origin]+= [casas_jogaveis]      
                                
      
                if coluna > 0 and linha > 0:
                    if matriz[linha-1][coluna-1] in 'pP':
                        if coluna > 1 and linha > 1:
                            if matriz[linha-2][coluna-2] == ' ':
                                print("b")
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                casas_origin = str(conjunto_de_pedras_posivel_de_comer) 
                    
                                casas_jogaveis = linha-2 , coluna-2
            
                                if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                    pedras_brancas_possiveis_de_comer[casas_origin] = [casas_jogaveis]
                                else:
                                    pedras_brancas_possiveis_de_comer[casas_origin]+= [casas_jogaveis]  
                if coluna < 7 and linha < 7:
                    
                    if matriz[linha+1][coluna+1]  in 'pP':
                        
                        if coluna < 6 and linha < 6:
                            if matriz[linha+2][coluna+2] == ' ':
                                print("c")
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                casas_origin = str(conjunto_de_pedras_posivel_de_comer) 
                    
                                casas_jogaveis = linha+2 , coluna+2
            
                                if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                    pedras_brancas_possiveis_de_comer[casas_origin] = [casas_jogaveis]
                                else:
                                    pedras_brancas_possiveis_de_comer[casas_origin]+= [casas_jogaveis]  
                            
                if coluna > 0 and linha < 7:
                    if matriz[linha+1][coluna-1] in 'pP' :
                        if coluna > 1 and linha  < 6:
                            if matriz[linha+2][coluna-2] ==' ':
                                print("d")
                                
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                casas_origin = str(conjunto_de_pedras_posivel_de_comer) 
                    
                                casas_jogaveis = linha+2 , coluna-2
            
                                if pedras_brancas_possiveis_de_comer.get(casas_origin) is None:
                                    pedras_brancas_possiveis_de_comer[casas_origin] = [casas_jogaveis]
                                else:
                                    pedras_brancas_possiveis_de_comer[casas_origin]+= [casas_jogaveis]  
                                    
                                    
    return pedras_brancas_possiveis_de_comer

def pedras_brancas_possiveis_de_comerer_dama(matriz):
    
    posissoes_pedras_pretas_para_brancas_comer= dict()
    

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'B':#dama
                        linha1 = linha2 = linha3 = linha4 =linha
                        coluna1 = coluna2 = coluna3 = coluna4 = coluna 

                        while True:#subir para direita 
                            if not ((linha1 > 0 and linha1 <7) and (coluna1 > 0 and coluna1 <7)) :
                                    break
                            if matriz[linha1][coluna1] in'Pp':#subir para direita   
                                
                                    
                                    
                                if matriz[linha1-1][coluna1+1] == ' ':               
                                    while(not (matriz[linha1-1][coluna1+1] !=' ')):
                                    
                                        conjunto_de_pedras_posivel_de_comer = linha,coluna
                                        casas_origin = str(conjunto_de_pedras_posivel_de_comer) 
                        
                                        casas_jogaveis = linha1 , coluna1
                
                                        if posissoes_pedras_pretas_para_brancas_comer.get(casas_origin) is None:
                                            posissoes_pedras_pretas_para_brancas_comer[casas_origin] = [casas_jogaveis]
                                        else:
                                            posissoes_pedras_pretas_para_brancas_comer[casas_origin]+= [casas_jogaveis] 

                                
                                
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
                
    return posissoes_pedras_pretas_para_brancas_comer  
print(pedras_brancas_possiveis_de_comerer_dama(matriz))