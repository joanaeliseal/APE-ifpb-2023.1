# Faça um programa que calcule e mostre o fatorial de um número N, fornecido pelo usuário.

N = int(input('Digite um número: '))
fatorial = 1

for i in range(2,N+1):
    fatorial*=i

print(f'{N}! = {fatorial}')