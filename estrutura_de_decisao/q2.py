# Escreva um programa que leia dois números e exiba-os em ordem crescente

num1 = int(input("Digite o 1o número: "))
num2 = int(input("Digite o 2o número: "))


if num1 < num2:
    print(f"Ordem crescente é {num1} e {num2}")
else:
    print(f"Ordem decrescente é {num2} e {num1}")