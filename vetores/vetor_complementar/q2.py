from random import randint

N = int(input('Tamanho do vetor: '))

vetor_a = [None]*N
vetor_b = [None]*N
vetor_c = [None]*N*2

#Gerando os vetores
for i in range(N):
    vetor_a[i] = randint(1,20)
for j in range(N):
    vetor_b[i] = randint(1,20)
for k in range(N):
    vetor_c[i*2] = vetor_a[i]
    vetor_c[i*2+1] = vetor_b[i]

# Imprimindo os vetores

print(f'Vetor A: {vetor_a}')
print(f'Vetor B: {vetor_b}')
print(f'Vetor C: {vetor_c}')