# 2) Faça um programa que leia um número N, inteiro, e some todos os números
# de 1 até N, mostrando o resultado.

N = int(input('Digite um número: '))
soma = 0

for i in range(1,N+1):
    soma += i
print(f'Somatório: {soma}')