# Escreva um programa que leia 3 números inteiros, determine e mostre o maior deles

num1 = int(input("Digite o 1o número: "))
num2 = int(input("Digite o 2o número: "))
num3 = int(input("Digite o 3o número: "))

if num1>num2 and num1>num3:
    print(f"O maior número é: {num1}")
elif num2>num1 and num2>num3:
    print(f"O número maior é: {num2}")
else:
    print(f"O número maior é: {num3}")

print("Fim do programa.")