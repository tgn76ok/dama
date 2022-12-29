import os 
matriz1 = [    ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
              [' ', 'p', ' ', 'p', ' ', 'p', ' ', 'p'],
              ['p', ' ', 'p', ' ', 'p', ' ', 'p', ' '],
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
    
    posicoes_possiveis_das_brancas = list()
    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'b':# posiçao de todas as brancas
                
                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna
                        
                        conjunto_de_jogadas = linha-1,coluna+1
                        if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                            posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)
                            
                        if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            pedras_brancas.append(conjunto_de_pedras_posivel_jogada)
                        
                
                        
                            
                if coluna != 0 and linha != 0 :
                    if matriz[linha-1][coluna-1] == ' ':
                        
                        conjunto_de_pedras_posivel_jogada = linha, coluna
                        
                        
                        conjunto_de_jogadas = linha-1,coluna-1
                        if conjunto_de_jogadas  not in  posicoes_possiveis_das_brancas:
                            posicoes_possiveis_das_brancas.append(conjunto_de_jogadas)
                            
                        if conjunto_de_pedras_posivel_jogada not in pedras_brancas:
                            pedras_brancas.append(conjunto_de_pedras_posivel_jogada)                
                    
                        
                        
                        
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
    else:
        print("erro essa pedra nao é branca")
        exit()             
                                       
                 
                        
    return posicoes_possiveis_das_brancas
    

def pedras_petras_possiveis_de_mover_sem_comer(matriz):
    
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
                            
                               
    return pedras_pretas

def posiçoes_possiveis_petras(matriz,posçoes_da_pedra):
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    
    posicoes_possiveis_das_petras = list()
    
    if matriz[linha][coluna] == 'p':# posiçao de todas as petras
        
        if coluna != 7 :
            if matriz[linha+1][coluna+1] == ' ':
                
                
                conjunto_de_jogadas = linha+1,coluna+1
                if conjunto_de_jogadas  not in  posicoes_possiveis_das_petras:
                    posicoes_possiveis_das_petras.append(conjunto_de_jogadas)
                    
                
        if coluna != 0:
            if matriz[linha+1][coluna-1] == ' ':
                
                
                
                conjunto_de_jogadas = linha+1,coluna-1
                if conjunto_de_jogadas  not in  posicoes_possiveis_das_petras:
                    posicoes_possiveis_das_petras.append(conjunto_de_jogadas)
    else:
        print("erro essa pedra nao é branca")
        exit()             
                                       
                 
                        
    return posicoes_possiveis_das_petras

def pode_comer_para_brancas(matriz):
    matriz = list(matriz)
    
    pedras_brancas_possiveis_de_comer= list()
    

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'b':# posiçao de todas as brancas

                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] == 'p':
                        if coluna != 6 and linha != 1:
                            if matriz[linha-2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
      
                if coluna != 0 and linha != 0:
                    if matriz[linha-1][coluna-1] == 'p':
                        if coluna != 1 and linha != 1:
                            if matriz[linha-2][coluna-2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 7 and linha != 7:
                    if matriz[linha+1][coluna+1] == 'p':
                        if coluna != 6 and linha != 6:
                            if matriz[linha+2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 0 and linha != 7:
                    if matriz[linha+1][coluna-1] == 'p':
                        if coluna != 1 and linha != 6:
                            if matriz[linha+2][coluna-2] ==' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_brancas_possiveis_de_comer:
                                    pedras_brancas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                
    return pedras_brancas_possiveis_de_comer  
        
def posiçoes_possiveis_para_comer_brancas(matriz,posçoes_da_pedra):
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    pedras_brancas_posisao_de_comer= list()
    pedras_petras_para_apagar= list()



    if matriz[linha][coluna] == 'b':# posiçao de todas as brancas

        if coluna != 7 and linha != 0 :
            if matriz[linha-1][coluna+1] == 'p':
                if coluna != 6 and linha != 1:
                    if matriz[linha-2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_petras_para_apagar:
                            pedras_petras_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

        if coluna != 0 and linha != 0:
            if matriz[linha-1][coluna-1] == 'p':
                if coluna != 1 and linha != 1:
                    if matriz[linha-2][coluna-2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna-2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_petras_para_apagar:
                            pedras_petras_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 7 and linha != 7:
            if matriz[linha+1][coluna+1] == 'p':
                if coluna != 6 and linha != 6:
                    if matriz[linha+2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_petras_para_apagar:
                            pedras_petras_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 0 and linha != 7:
            if matriz[linha+1][coluna-1] == 'p':
                if coluna != 1 and linha != 6:
                    if matriz[linha+2][coluna-2] ==' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna-2
                        
                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_brancas_posisao_de_comer:
                            pedras_brancas_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_petras_para_apagar:
                            pedras_petras_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                            
                        
        
    return (pedras_brancas_posisao_de_comer,pedras_petras_para_apagar)
                                                
def pode_comer_para_pretas(matriz):
    matriz = list(matriz)
    
    pedras_pretas_possiveis_de_comer= list()
    

    for linha in range(len(matriz)):
        for coluna in range(len(matriz)):
            if matriz[linha][coluna] == 'p':# posiçao de todas as petras

                if coluna != 7 and linha != 0 :
                    if matriz[linha-1][coluna+1] == 'b':
                        if coluna != 6 and linha != 1:
                            if matriz[linha-2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
      
                if coluna != 0 and linha != 0:
                    if matriz[linha-1][coluna-1] == 'b':
                        if coluna != 1 and linha != 1:
                            if matriz[linha-2][coluna-2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 7 and linha != 7:
                    if matriz[linha+1][coluna+1] == 'b':
                        if coluna != 6 and linha != 6:
                            if matriz[linha+2][coluna+2] == ' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                            
                if coluna != 0 and linha != 7:
                    if matriz[linha+1][coluna-1] == 'b':
                        if coluna != 1 and linha != 6:
                            if matriz[linha+2][coluna-2] ==' ':
                                conjunto_de_pedras_posivel_de_comer = linha, coluna

                                if conjunto_de_pedras_posivel_de_comer not in pedras_pretas_possiveis_de_comer:
                                    pedras_pretas_possiveis_de_comer.append(conjunto_de_pedras_posivel_de_comer)
                
    return pedras_pretas_possiveis_de_comer  
        
def posiçoes_possiveis_para_comer_pretas(matriz,posçoes_da_pedra):
    matriz = list(matriz)
    linha , coluna = posçoes_da_pedra
    pedras_petras_posisao_de_comer= list()
    pedras_brancas_para_apagar= list()



    if matriz[linha][coluna] == 'p':# posiçao de todas as brancas

        if coluna != 7 and linha != 0 :
            if matriz[linha-1][coluna+1] == 'b':
                if coluna != 6 and linha != 1:
                    if matriz[linha-2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_petras_posisao_de_comer:
                            pedras_petras_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)

        if coluna != 0 and linha != 0:
            if matriz[linha-1][coluna-1] == 'b':
                if coluna != 1 and linha != 1:
                    if matriz[linha-2][coluna-2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha-2, coluna-2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_petras_posisao_de_comer:
                            pedras_petras_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha-1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 7 and linha != 7:
            if matriz[linha+1][coluna+1] == 'b':
                if coluna != 6 and linha != 6:
                    if matriz[linha+2][coluna+2] == ' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna+2

                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_petras_posisao_de_comer:
                            pedras_petras_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                        
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna+1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                    
        if coluna != 0 and linha != 7:
            if matriz[linha+1][coluna-1] == 'b':
                if coluna != 1 and linha != 6:
                    if matriz[linha+2][coluna-2] ==' ':
                        conjunto_de_posiçoes_pedras_posivel_de_comer = linha+2, coluna-2
                        
                        if conjunto_de_posiçoes_pedras_posivel_de_comer not in pedras_petras_posisao_de_comer:
                            pedras_petras_posisao_de_comer.append(conjunto_de_posiçoes_pedras_posivel_de_comer)
                            
                        conjunto_de_posiçoes_pedras_para_apagar = linha+1, coluna-1

                        if conjunto_de_posiçoes_pedras_para_apagar not in pedras_brancas_para_apagar:
                            pedras_brancas_para_apagar.append(conjunto_de_posiçoes_pedras_para_apagar)
                            
                        
        
    return (pedras_petras_posisao_de_comer,pedras_brancas_para_apagar)

   
turno=0
cont = 0
pedra_para_comer_petra = pode_comer_para_pretas(matriz1)

pedra_para_comer_branca = pode_comer_para_brancas(matriz1)

while True:
    os.system("cls")
    print(f"-------------------------------------------")
    print(f"{matriz1[0]}\n{matriz1[1]}\n{matriz1[2]}\n{matriz1[3]}\n{matriz1[4]}\n{matriz1[5]}\n{matriz1[6]}\n{matriz1[7]}\n")
   
    if turno %2 ==0:
        
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
            
            matriz1[pedra_escolhida_pelo_jogador_1[0]][pedra_escolhida_pelo_jogador_1[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_1[0]][jogada_escolhida_pelo_jogador_1[1]]= 'b'

            turno+=1
    
        else:
            print(f"Escolha uma das pedras brancas para comer outra petra, pelo numero com respodente")
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
            
            matriz1[pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1[0]][pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_1[1]]= ' '
            matriz1[pedra_escolhida_para_apagar[0]][pedra_escolhida_para_apagar[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_1_para_comer[0]][jogada_escolhida_pelo_jogador_1_para_comer[1]]= 'b'
            
        
            
    else:
        
        if len(pedra_para_comer_petra) == 0:
            pedras_pretas = pedras_petras_possiveis_de_mover_sem_comer(matriz1)


            print(f"Escolha uma das pedras petras para andar, pelo numero conrespodente")
            for i in pedras_pretas: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont= 0
            
            index_para_pegar_a_pedra= int(input(">>"))
            pedra_escolhida_pelo_jogador_2=pedras_pretas[index_para_pegar_a_pedra]
            posiçao_das_posiveis_jogadas = posiçoes_possiveis_petras(matriz1,pedra_escolhida_pelo_jogador_2)
            
            
            print("agora escolha aonde voce quer jogar")
            for i in posiçao_das_posiveis_jogadas: print(f"{cont}. posiçao-{i}"); cont+=1 
            
            cont = 0 
            index_para_pegar_a_jogada= int(input(">>"))
            jogada_escolhida_pelo_jogador_2=posiçao_das_posiveis_jogadas[index_para_pegar_a_jogada]
            
            matriz1[pedra_escolhida_pelo_jogador_2[0]][pedra_escolhida_pelo_jogador_2[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_2[0]][jogada_escolhida_pelo_jogador_2[1]]= 'p'

            turno+=1

            
        else:
            print(f"Escolha uma das pedras para comer uma branca, pelo numero com respodente 3")
            for i in pedra_para_comer_petra: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont = 0 
            
            
            index_para_pegar_a_pedra= int(input(">>"))
            pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2=pedra_para_comer_petra[index_para_pegar_a_pedra]
            
            posiçao_das_posiveis_jogadas_para_comer_petras,pedras_brancas_para_apagar = posiçoes_possiveis_para_comer_pretas(matriz1,pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2)
            
            print("agora escolha aonde voce quer jogar")
            
            for i in posiçao_das_posiveis_jogadas_para_comer_petras: print(f"{cont}. posiçao-{i}"); cont+=1 
            cont = 0 
            
            
            index_para_pegar_a_jogada= int(input(">>"))
            jogada_escolhida_pelo_jogador_2_para_comer=posiçao_das_posiveis_jogadas_para_comer_petras[index_para_pegar_a_jogada]
            pedra_escolhida_para_apagar = pedras_brancas_para_apagar[index_para_pegar_a_jogada]
            
            matriz1[pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2[0]][pedra_com_posibilidade_de_comer_escolhida_pelo_jogador_2[1]]= ' '
            matriz1[pedra_escolhida_para_apagar[0]][pedra_escolhida_para_apagar[1]]= ' '
            matriz1[jogada_escolhida_pelo_jogador_2_para_comer[0]][jogada_escolhida_pelo_jogador_2_para_comer[1]]= 'p'
    
    