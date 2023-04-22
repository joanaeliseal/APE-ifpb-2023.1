#Faça um programa que calcule e mostre os números múltiplos de 5 do
#intervalo 50 a 300, juntamente com suas raízes e seus cubos.

import math
#Gerando os múltiplos entre 50 e 300
cont = 0
for k in range(50,301,5):
    print(f'Raiz={math.sqrt(k):.2f}; cubo={k**3:.2f}')
    cont += 1
print(f'Foram gerados {cont} múltiplos de 5')