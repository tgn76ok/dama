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
matriz3 = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'p', ' ', ' ', ' ', 'p', ' ', ' '],
              [' ', ' ', 'b', ' ', 'b', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               #0    1    2    3    4    5    6    7 
]
matriz = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', 'B', ' ', ' ', ' ', ' ', ' '],
              [' ', 'p', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
               #0    1    2    3    4    5    6    7 
]
matriz4 = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'b', ' ', ' ', ' ', ' ', 'b', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['b', ' ', ' ', ' ', ' ', 'b', ' ', 'b'],
               #0    1    2    3    4    5    6    7 
]
matriz4 = [    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', 'p', ' ', ' ', ' ', ' ', 'p', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
              ['p', ' ', ' ', ' ', ' ', 'p', ' ', 'p'],
               #0    1    2    3    4    5    6    7 
]
linha = 4
coluna= 2
linha1 = linha
coluna1 = coluna
pedras_brancas_possiveis_de_comer = list()
print(matriz[linha][coluna])


          
linha1 = linha2 = linha3 = linha4 =linha
coluna1 = coluna2 = coluna3 = coluna4 = coluna 

while True:#subir para direita 
    if not ( (linha1 != 0 and linha1 !=7) and (coluna1 != 0 and coluna1 !=7)) :
            break
    if matriz[linha1][coluna1] == 'p':#subir para direita       
        if matriz[linha1-1][coluna1+1] == ' ':               
            
            
            conjunto_de_pedras_posivel_de_comer = linha,coluna
            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

        
        
    linha1-=1
    coluna1+=1
while True:#subir para direita 
    if not ( (linha2 != 0 and linha2 !=7) and (coluna2 != 0 and coluna2 !=7)) :
            break
    if matriz[linha2][coluna2] == 'p':#subir para direita       
        if matriz[linha2-1][coluna2+1] == ' ':               
            
            
            conjunto_de_pedras_posivel_de_comer = linha,coluna
            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

        
        
    linha2-=1
    coluna2-=1
while True:#subir para direita   
    if not ( (linha3 != 0 and linha3 !=7) and (coluna3 != 0 and coluna3 !=7)) :
        break
    if matriz[linha3][coluna3] == 'p':#subir para direita       
        print(1)
        if matriz[linha3-1][coluna3+1] == ' ':               
            
            
            conjunto_de_pedras_posivel_de_comer = linha,coluna
            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

        
        
    linha3+=1
    coluna3-=1
while True:#subir para direita   
    if not ( (linha4 != 0 and linha4 !=7) and (coluna4 != 0 and coluna4 !=7)) :
            break
    if matriz[linha4][coluna4] == 'p':#subir para direita       
        if matriz[linha4-1][coluna4+1] == ' ':               
            
            
            conjunto_de_pedras_posivel_de_comer = linha,coluna
            if conjunto_de_pedras_posivel_de_comer  not in  pedras_brancas_possiveis_de_comer:
                pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)

        
        
    linha4+=1
    coluna4+=1           
        
        
# while matriz[linha2][coluna2] == 'B' or matriz[linha2][coluna2] == ' ':

#     if matriz[linha2][coluna2] == ' ':#subir para esqurda

        
#         conjunto_de_jogadas = linha2,coluna2
#         if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
#             posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
#         if not ( (linha2 != 0 and linha2 !=7) and (coluna2 != 0 and coluna2 !=7)) :
#             break
        
#     linha2-=1
#     coluna2-=1
# while matriz[linha3][coluna3] == 'B' or matriz[linha3][coluna3] == ' ':

#     if matriz[linha3][coluna3] == ' ':#baixo para esqurda
        

#         conjunto_de_jogadas = linha3,coluna3
#         if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
#             posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
#         if not ( (linha3 != 0 and linha3 !=7) and (coluna3 != 0 and coluna3 !=7)) :
#             break
        
#     linha3+=1
#     coluna3-=1
# while matriz[linha4][coluna4] == 'B' or matriz[linha4][coluna4] == ' ':

#     if matriz[linha4][coluna4] == ' ':#baixo para direita
        

        
#         conjunto_de_jogadas = linha4,coluna4
#         if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
#             posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)

        
#         if not ( (linha4 != 0 and linha4 !=7) and (coluna4 != 0 and coluna4 !=7)) :
#             break
        
#     linha4+=1
#     coluna4+=1
                    
print(pedras_brancas_possiveis_de_comer)