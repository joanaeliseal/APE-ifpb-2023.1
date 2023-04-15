'''Escreva um programa que tenha a funcionalidade de uma calculadora simples. O programa deve
solicitar a digitação de dois operandos e um operador (+ - x * / %) e deve imprimir ao resultado
da operação aritmética. Caso o usuário digite um operador inválido, o programa deve imprimir
"Operador desconhecido".'''
# Resolução usando Match Pattern

num1 = float(input('Digite um número: '))
operador = input('Digite um operador: ').lower()
num2 = float(input('Digite um número: '))

match operador:
    case '+':
        print(f'{num1}+{num2}={num1+num2:1f}')
    case '-':
        print(f'{num1}-{num2}={num1-num2:.1f}')
    case 'x' | '*':
        print(f'{num1}x{num2}={num1*num2:.1f}')
    case '*':
        print(f'{num1}*{num2}={num1**num2:.1f}')
    case '/':
        if num2!=0: 
            print(f'{num1}/{num2}={num1/num2}')
    case '%':
        if num2!=0:
            print(f'{num1}%{num2}={num1%num2}')
    case _: #convenção colocar um underline
        print('Operador inválido!')