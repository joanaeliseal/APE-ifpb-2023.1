# O restaurante a quilo Bem-Bão cobra R$25,00 por cada quilo de refeição. Faça um
# programa que leia o peso do prato montado pelo cliente (em quilos) e exiba o valor
# a pagar. Assuma que a balança já desconte o peso do prato.

peso = float(input("Informe o peso do prato em kg: "))
prato = peso*25.00

print(f"O peso do prato é {peso:.2f}kg e o valor a pagar é R${prato:.2f}")

# Constantes escrever todo em maiúsculo, o código entende que é const
# VALOR_KG = 25