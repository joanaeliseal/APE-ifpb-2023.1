# Recomendam-se estudantes para bolsas de estudo em função de seu desempenho.
# A natureza das recomendações é baseada na seguinte tabela:
# A: fortemente recomendado
# B ou C: recomendado
# D: não recomendado

nome = input('Digite o nome do estudante: ')
conceito = input('Digite o desempenho do estudante (conceito): ').upper()

if conceito == 'A':
    print('Fortemente recomendado')
elif conceito == 'B' or conceito=='C':
    print('Recomendado')
else:
    print('Não recomendado')