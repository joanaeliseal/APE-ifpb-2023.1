'''Escreva um programa que solicite a digitação de um número (de 1 a 7) correspondente a um dia
da semana e imprima o nome do dia da semana e se é dia útil (de segunda a sexta) ou final de
semana (sábado e domingo). Considere que o dia 1 é o domingo.'''
# Resolvido com Match Pattern
numero = int(input("Digite um número (1-7): "))

match numero:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case 7: 
        print('Sábado')
    case _:
        print('Valor inválido!')

print('Fim do programa')