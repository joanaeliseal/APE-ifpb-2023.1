# Escreva uma função chamada vogal que receba uma letra e verifique se a letra é uma vogal, retornando o valor True nesse caso, ou o valor False caso contrário.
#Escreva também um programa que leia uma frase e, usando a função vogal criada,
# imprima a quantidade de vogais existentes na frase lida.

def vogal(frase):
  for caracter in frase:
    if 'AEIOU':
      caracter = True
    else:
      caracter = False

letra = input('Digite uma frase: ').upper()

print(letra)
print(f'A frase contém {vogal(letra)} vogais')