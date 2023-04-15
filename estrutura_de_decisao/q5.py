# A empresa Vende Tudo Ltda paga o salário de cada vendedor com uma comissão de 5% sobre o
# total de vendas daquele vendedor, mas essa comissão nunca deve ser inferior ao salário-
# mínimo. Escreva um programa que leia o valor total das vendas de um vendedor e escreva seu
# salário.
# R$ 1.320

SALARIO_MINIMO = 1.350
COMISSAO = 0.05

total_vendas = float(input("Informe o total de vendas: "))

if total_vendas < SALARIO_MINIMO:
    print("A comissão é inferior ao salário mínimo!")
elif total_vendas >= SALARIO_MINIMO:
    salario_final = SALARIO_MINIMO + (COMISSAO*total_vendas)
    print(f"A sua comissão será de: {salario_final:.2f}")