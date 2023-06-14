#1. Escreva uma função chamada menor que receba 3 números e retorne o menor
#deles. Faça também um programa para testar a função.

#Função = sub-programa
def menor(v1,v2,v3):
  if v1<v2 and v1<v3:
    return v1
  elif v2<v1 and v2<v3:
    return v2
  else:
    return v3

#programa principal
a = int(input('Digite valor 1: '))
b = int(input('Digite valor 2: '))
c = int(input('Digite valor 3: '))

resultado = menor(a,b,c)
print('O menor é:')
print(resultado)