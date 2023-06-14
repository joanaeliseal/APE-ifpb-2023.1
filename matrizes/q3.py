# Escreva um programa que gere aleatoriamente uma matriz quadrada A (cuja ordem
# será lida) e gere uma matriz B (da mesma ordem de A), onde cada elemento de B
# corresponderá ao respectivo elemento de A somado a ele os seus índices, sendo que se
# o elemento for de alguma diagonal (principal ou secundária) deverá ser colocado 0
# (zero).
from random import randint


ordem = int(input('Digite a ordem da matriz quadrada: '))
COLUNA = LINHA = ordem

matriz_a = [[None]*COLUNA for i in range(LINHA)]
matriz_b = [[None]*COLUNA for i in range(LINHA)]

#gerando a matriz A
print('Matriz A')
for linha in range(LINHA):
    for coluna in range(COLUNA):
        matriz_a[linha][coluna]=randint(1,10)

#gimprimindo a matriz A
for linha in range(LINHA):
    for coluna in range(COLUNA):
        print(f'{matriz_a[linha][coluna]:4}', end='')
    print()

# se a matriz for secundária ou principal
print('Matriz B')
for linha in range(LINHA):
    for coluna in range(COLUNA):
        if linha==coluna or linha+coluna==ordem-1:
            matriz_b[linha][coluna]=0
        else:
            matriz_b[linha][coluna]=matriz_a[linha][coluna]+linha+coluna

#gimprimindo a matriz B
for linha in range(LINHA):
    for coluna in range(COLUNA):
        print(f'{matriz_b[linha][coluna]:4}', end='')
    print()