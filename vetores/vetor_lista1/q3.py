# Escreva um programa que leia um vetor V contendo N elementos inteiros (N será
#lido) e um valor inteiro K, verifique e exiba se o K está ou não no vetor. Se estiver,
#informe em que posição (índice).
#Obs: K pode se repetir no vetor, nesse caso, mostre todas as posições onde o K
#aparece.

N = 0
vetor = [None]*N
cont_k = 0
posicao = [None]

N = int(input('Quantos N elementos: '))

for k in range(N+1):
    vetor[k] = int(input('Digite um número: '))
    if vetor[k]==k:
        cont_k+=1
        posicao = k
    
print(f'O número {vetor[k]} aparece {cont_k} vezes na(s) posição(ões) {posicao}')