matriz2 = [    ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
              [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
              ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
              ['b', ' ', 'b', ' ', 'b', ' ', 'b', ' '],
              [' ', 'b', ' ', 'b', ' ', 'b', ' ', 'b'],
               #0    1    2    3    4    5    6    7 
]
matriz = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', 'B', ' '],
              [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', 'B', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               #0    1    2    3    4    5    6    7 
]


posicoes_possiveis_das_brancas_sem_comer={}
posicoes_possiveis_das_brancas = list()



          
linha1 = linha2 = linha3 = linha4 =linha
coluna1 = coluna2 = coluna3 = coluna4 = coluna 

while matriz[linha1][coluna1] == 'B' or matriz[linha1][coluna1] == ' ':
    if matriz[linha1][coluna1] == 'B': x_origin ,y_origini = linha1,coluna1
    if matriz[linha1][coluna1] == ' ':#subir para direita
        

        
        conjunto_de_jogadas = linha1,coluna1
        
        if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
            
            casas_origin = str((x_origin , y_origini))
            
            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [conjunto_de_jogadas]
            else:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [conjunto_de_jogadas]
            
            posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
        if not ( (linha1 != 0 and linha1 !=7) and (coluna1 != 0 and coluna1 !=7)) :
            break
        
    linha1-=1
    coluna1+=1
while matriz[linha2][coluna2] == 'B' or matriz[linha2][coluna2] == ' ':

    if matriz[linha2][coluna2] == 'B': x_origin ,y_origini = linha2,coluna2
    if matriz[linha2][coluna2] == ' ':#subir para esqurda

        
        conjunto_de_jogadas = linha2,coluna2
        if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
            
            
            casas_origin = str((x_origin , y_origini))
            
            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [conjunto_de_jogadas]
            else:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [conjunto_de_jogadas]
            
            
            posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
        if not ( (linha2 != 0 and linha2 !=7) and (coluna2 != 0 and coluna2 !=7)) :
            break
        
    linha2-=1
    coluna2-=1
while matriz[linha3][coluna3] == 'B' or matriz[linha3][coluna3] == ' ':
    if matriz[linha3][coluna3] == 'B': x_origin ,y_origini = linha3,coluna3

    if matriz[linha3][coluna3] == ' ':#baixo para esqurda
        

        conjunto_de_jogadas = linha3,coluna3
        if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
            
            casas_origin = str((x_origin , y_origini))
            
            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [conjunto_de_jogadas]
            else:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [conjunto_de_jogadas]
            
            posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
        if not ( (linha3 != 0 and linha3 !=7) and (coluna3 != 0 and coluna3 !=7)) :
            break
        
    linha3+=1
    coluna3-=1
while matriz[linha4][coluna4] == 'B' or matriz[linha4][coluna4] == ' ':
    if matriz[linha4][coluna4] == 'B': x_origin ,y_origini = linha4,coluna4

    if matriz[linha4][coluna4] == ' ':#baixo para direita
        

        
        conjunto_de_jogadas = linha4,coluna4
        if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
            
            
            casas_origin = str((x_origin , y_origini))
            
            if posicoes_possiveis_das_brancas_sem_comer.get(casas_origin) is None:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin] = [conjunto_de_jogadas]
            else:
                posicoes_possiveis_das_brancas_sem_comer[casas_origin]+= [conjunto_de_jogadas]
            
            posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
        if not ( (linha4 != 0 and linha4 !=7) and (coluna4 != 0 and coluna4 !=7)) :
            break
        
    linha4+=1
    coluna4+=1
                    
print(posicoes_possiveis_das_brancas)
print(posicoes_possiveis_das_brancas_sem_comer)