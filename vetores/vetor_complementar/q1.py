N = int(input('Número do vetor: '))

vetor = [None]*N

for i in range(N):
    vetor[i] = int(input('Digite um número: '))

cont_par = cont_impar = soma = 0

for i in range(N):
    if vetor[i]%2==0:
        cont_par +=1
    else:
        cont_impar +=1

for i in range(N):
    soma +=1

media = soma/N

print(f'São {cont_par} números pares')
print(f'São {cont_impar} números ímpares')
print(f'Soma: {soma}')
print(f'Média dos elementos: {media}')