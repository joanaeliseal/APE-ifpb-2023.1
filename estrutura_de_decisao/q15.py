# Escreva um programa para determinar as raízes de uma equação de segundo grau, dados os
# seus coeficientes. Fórmulas:
# Obs: se Δ for negativo, não existem as raízes da equação.
# Dica: use a função sqrt do módulo math.
import math

print('Entre com os coeficientes da equação de 2º grau:')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

delta = (b**2) - (4*a*c)

if delta < 0:
    print('Não existem raízes reais para a equação!')
else:
    x1 = (-b + math.sqrt(delta)) / 2*a 
    x2 = (-b - math.sqrt(delta)) / 2*a
    print(f'As raízes são: {x1:.1f} e {x2:.1f}')