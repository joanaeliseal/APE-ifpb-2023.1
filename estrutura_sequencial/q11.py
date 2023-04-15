# Escreva um programa que leia duas variáveis inteiras e troque o conteúdo entre elas,
# mostrando o resultado.

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
temp = 0

temp = num1
num1 = num2
num2 = temp

print(f"O primeiro número vai receber {num1} e o segundo vai receber {num2} ")

# a,b=b,a (swap: trocar conteúdo entre células)
# x,z,y=7,8,9
# x=z=y=10
# Python faz o swap