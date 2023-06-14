# Escreva um programa que:
#• Leia (ou gere aleatoriamente) uma matriz quadrada de ordem N contendo elementos
#inteiros (N será lido);
#• Exiba a matriz lida (no formato de matriz);
#• Exiba os elementos da diagonal principal, isto é, os elementos onde I = J.

from random import randint


N = int(input('Digite a ordem da matriz quadrada: '))
COLUNA = LINHA = N

matriz = [[None]*COLUNA for i in range(LINHA)]

#gerando a matriz
for linha in range(LINHA):
    for coluna in range(COLUNA):
        matriz[linha][coluna]=randint(1,100)
        print(f'{matriz[linha][coluna]:4}', end='')
    print()

# matriz quadrada
print('Elementos da diagonal principal')
for linha in range(LINHA):
    for coluna in range(COLUNA):
        if linha==coluna:
            print(f'{matriz[linha][coluna]:4}', end='')