# Escreva um programa que leia um vetor V (contendo 30 inteiros) e um valor
#inteiro K, calcule e exiba a quantidade de ocorrências de K dentro de V.

cont = 0
n = 10
vetor = [None]*n

for k in range(n):
    vetor = int(input('Digite um número: '))
    if vetor==k:
        cont+=k

print(f'Contagem final: {cont}')