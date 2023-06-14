#Escreva um programa que preencha duas matrizes (A e B), ambas de ordem 2x3, com
#valores inteiros fornecidos pelo usuário (ou gerados aleatoriamente). O programa
#deverá somar as duas matrizes, armazenando o resultado em uma terceira matriz (C).
#Ao final, exiba as 3 matrizes (no formato de matriz).

import random 

LINHAS = 2
COLUNAS = 3

matriz_a = [[random.randint(1,100) for j in range(COLUNAS)] for i in range(LINHAS)]
matriz_b = [[random.randint(1,100) for j in range(COLUNAS)] for i in range(LINHAS)]
matriz_c = [[random.randint(1,100) for j in range(COLUNAS)] for i in range(LINHAS)]

#matriz_a = [[None]*COLUNAS for i in range(LINHAS)]
#matriz_b = [[None]*COLUNAS for i in range(LINHAS)]
#matriz_c = [[None]*COLUNAS for i in range(LINHAS)]

#gerando a matriz A
print('Matriz A gerada: ')
for i in range(LINHAS):
    for j in range(COLUNAS):
        print(f'{matriz_a[i][j]:4}', end='')
    print()

# gerando a matriz B
print('Matriz B gerada: ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        print(f'{matriz_b[linha][coluna]:4}', end='')
    print()

# gerando a soma (matriz C)
print('Matriz C (soma): ')
for linha in range(LINHAS):
    for coluna in range(COLUNAS):
        matriz_c[linha][coluna]=matriz_a[linha][coluna]+matriz_b[linha][coluna]
        print(f'{matriz_c[linha][coluna]:4}', end='')
    print()