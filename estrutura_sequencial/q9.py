# A Companhia de Carros Usados João Honesto paga seus empregados um salário de R$
#1.000,00 por mês mais uma comissão de R$ 200,00 por cada carro vendido mais 5% do
# valor da venda.
# Escreva um programa que leia o nome, o número de carros vendidos e o valor total das
# vendas de um vendedor, e calcule e exiba o seu salário.

SALARIO_BASE = 1000.00
COMISSAO = 200.00
PERCENT = 0.05

nome_empregado = input("Informe o nome do funcionário: ")
carros_vendidos = int(input("Informe o valor de carros vendidos pelo funcionário: "))
valor_venda = float(input("Informe o valor do carro vendido: "))

salario_final = SALARIO_BASE + (COMISSAO*carros_vendidos) + (valor_venda*PERCENT)

print(f"Funcionário: {nome_empregado}")
print(f"Número de carros vendidos: {carros_vendidos}")
print(f"Valor total das vendas com salário: {salario_final:.2f}")