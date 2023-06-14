# Escreva um programa que leia 10 números e armazene-os em um vetor. Exiba:
#     • Os números que estão nos índices pares;
#     • Os números que estão nos índices ímpares.

vetor = [None]*10

for index in range(10):
    if index % 2==0: