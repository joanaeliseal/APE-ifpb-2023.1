# Uma matriz transposta é a matriz que se obtém da troca de linhas por colunas de uma
# dada matriz.
# Assim, dada uma matriz C de ordem m x n, a matriz transposta dela será representada
# por Ct de ordem n x m, onde cada elemento de Ct[i,j] = C[j,i].
# Escreva um programa que preencha uma matriz 3x5 com valores inteiros fornecidos
# pelo usuário (ou gerados aleatoriamente) e gere a sua transposta. Ao final, imprima as
# duas matrizes (no formato de matriz).

from random import randint

ORDEM_M = 3 #linha
ORDEM_N = 5 #coluna

# criação das matrizes
matriz = [[None]*ORDEM_N for i in range(ORDEM_M)] 
matriz_t = [[None]*ORDEM_N for i in range(ORDEM_N)] 

# gerando a matriz
print('Matriz')
for linha in range(ORDEM_M):
    for coluna in range(ORDEM_N):
        matriz[linha][coluna]=randint(1,100)
        print(f'{matriz[linha][coluna]:4}', end='')
    print()

# Geração da matriz T (transposta)
for i in range(ORDEM_M):
    for j in range(ORDEM_N):
        matriz_t[j][i] = matriz[i][j]

# Impressão da matriz M
print('\nMatriz M:')
for i in range(ORDEM_M):
    for j in range(ORDEM_N):
        print(f'{matriz[i][j]:4}',end='')#do msm jeito q tu pensou otaria
    print()

# Impressão da matriz T
print('\nMatriz T (transposta):')
for i in range(ORDEM_N):  # pra deixar de ser otaria
    for j in range(ORDEM_M):
        print(f'{matriz_t[i][j]:4}',end='')
    print()






# imprimindo a porra da matriz
#for linha in range(ORDEM_M):
#    for coluna in range(ORDEM_N):
#        print(f'{matriz[linha][coluna]:4}', end='')
#    print()

# gerando a matriz transposta
#print('Matriz Transposta')
#matriz,*matriz_t = zip(*matriz)
#print(matriz_t)
#print()



#matriz_t = [[k[linha] for k in matriz] for j[coluna] in matriz] #solução usando list comprehension #swap
#matriz_t = list(map(list, zip(*matriz)))