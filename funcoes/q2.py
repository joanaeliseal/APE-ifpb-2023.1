# 2. Escreva uma função chamada fatorial que receba um número inteiro e retorne 
# seu fatorial. Faça também um programa para testar a função.

# Função
def fatorial(num):
  fat =1
  for i in range(2,num+1):
    fat *=i
  return fat

# testar função

numero = int(input('Digite o número: '))

print(f'{numero}!={fatorial(numero)}')