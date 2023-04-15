'''Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir
"Operador desconhecido".'''

num1 = float(input('Digite um número: '))
operador = input('Digite um operador: ')
num2 = float(input('Digite um número: '))

if operador == '+':
    print(f'{num1}+{num2}={num1+num2:1f}')
elif operador == '-':
    print(f'{num1}-{num2}={num1-num2:.1f}')
elif operador == 'x':
    print(f'{num1}x{num2}={num1*num2:.1f}')
elif operador == '*':
    print(f'{num1}*{num2}={num1**num2:.1f}')
elif operador == '/' and num2 !=0: 
    print(f'{num1}/{num2}={num1/num2}')
elif operador == '%' and num2 !=0:
    print(f'{num1}%{num2}={num1%num2}')
else:
    print('Operador inválido!')